<template>
  <div>
    <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <button
            type="button"
            class="navbar-toggle"
            data-toggle="collapse"
            data-target="#myNavbar"
          >
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <h2 class="navbar-brand" href="#">&nbsp;&nbsp;FRUIT STORE</h2><br>
          <a>{{showName}}</a>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav navbar-right">
            <li>
              <a>Home</a>
            </li>
            <li>
              <a>Transactions</a>
            </li>
            <li style="color:white">
              <a style="color:white" v-if="totalProducts !== 0">Total Price:{{ totalProducts }}</a>
            </li>
            <li>
              <a> <Icon type="ios-cart-outline" size="24" />{{ FruitCount }}</a>
            </li>
            <li>
              <a style="float:right;font-size:135%;" @click="logout">Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <br><br><br><br><br>
    <!-- <h2>Total Price:{{ totalProducts}}</h2> -->
    <center><br>
      <h1>Available Retailers</h1> <br><br>
      <div v-if="state === 'default'">
        <h4 v-for="(retailer,index) in showRetailers" :key="retailer.RetailerEmail">
             <div id="list">
               <h4>Retailer Name:  {{ retailer.RetailerName }}</h4>
               <h4>Retailer Email:  {{ retailer.RetailerEmail }}</h4>
               <br>
               <ButtonGroup size="large">
                  <Button type="info"
               @click="displayParticularRetailerFruits(index,retailer.RetailerEmail)">
               Show Fruits</Button>
               </ButtonGroup>
             </div>
        </h4>
      </div>
    </center>
    <br>
    <div v-if="state === 'showFruitsState'">
      <center>
        <ButtonGroup size="large">
          <Button type="info"
      @click="changeState('default')"
      style="text-align:center;">Close</Button>
        </ButtonGroup>
        </center>
        <center style="text-align:center;">
        <h4 v-for="product in products" :key="product.name">
          <center>
          <table border="0">
            <tr>
              <td>
                <div id="list">
                  <h4 id="productdisplay" style="float:right;color:#5ce61c;">Retailer:
                    {{ product.retailer_Email}}</h4>
                  <h4 id="productdisplay">Fruit: {{ product.name}}</h4>
                  <h4 id="productdisplay">Quantity: {{ product.quantity1}}</h4>
                  <h4 id="productdisplay">Rs: {{ product.price}}</h4>
                  <ButtonGroup>
                      <Button type="primary" @click="product.quantity = (product.quantity + 1 ),
                      storeCustomerClickedItems(product.name,
                  product.quantity1, product.price,
                product.quantity, product.retailer_Email)"
                  :disabled="product.quantity1 <= product.quantity || product.quantity1 ===0"
                  ><Icon type="md-add" size="20" /></Button>
                  </ButtonGroup>
                  <!-- <input
                    type="button"
                    id="bt1"
                    @click="product.quantity = (product.quantity + 1 )"
                    value="+"
                    class="btn btn-primary"
                    :disabled="product.quantity1 <= product.quantity || product.quantity1 ===0"
                  > -->
                  <input
                    type="text" value="0"
                    v-on:keypress="isNumber($event)"
                    style="color:blue"
                    name="quantity"
                    v-model.number="product.quantity" disabled
                  >
                  <ButtonGroup>
                      <Button type="primary" @click="product.quantity = (product.quantity - 1 ),
                      storeCustomerClickedItems(product.name,
                  product.quantity1, product.price,
                product.quantity, product.retailer_Email)"
                  :disabled="product.quantity <= 0 || product.quantity1 ===0"
                  ><Icon type="md-remove" size="20" /></Button>
                  </ButtonGroup>
                  <!-- <input
                    type="button"
                    id="bt2"
                    @click="product.quantity = (product.quantity - 1 )"
                    class="btn btn-primary"
                    value="-"
                    :disabled="product.quantity <= 0 || product.quantity1 ===0"
                  > -->
                  <br>
                  <p></p>
                  <span v-if="product.quantity1 === 0" style="color:red">OUT OF STOCK</span>
                </div>
              </td>
              <td id="secondDivision" v-if="product.quantity > 0"><br><br>
                <h3>PRODUCTS SUMMARY</h3>
                <br>
                <h4>{{product.name}}</h4>
                <p>
                  <br>
                  {{product.quantity}} x Rs {{product.price}}
                  = Rs {{product.quantity*product.price}}
                </p>
              </td>
            </tr>
          </table>
          </center>
        </h4>
        </center>
    </div>
    <h2 style="text-align:right;">Total Price:{{ totalProducts}}</h2>
    <br>
    <button v-if="totalProducts > 0" id="checkout" @click="show">
        Check Out Rs {{totalProducts}}</button>
    <br>
    <modal name="hello-world" :width="400" :height="100">
      <h3>Fruits will be delivered within two days</h3>
      <br>
      <br>
      <h4>Thanks For Purchasing... Have a nice day</h4>
    </modal>
  </div>
</template>

<script>

import axios from 'axios';

/* eslint-disable */
// const i = 1;
export default {
  data() {
    return {
      showRetailers : [],
      state: 'default',
      showFruitsBoolean : false,
      showRetailerBoolean: true,
      FruitCount: 0,
      products: [],
      customerClickedItemsToStoreInDb: [],
    };
  },
  computed: {
    totalProducts() {
      return this.products.reduce((sum, product) => {
        if (product.quantity1 < product.quantity) {
          this.product.quantity = product.quantity1;
          this.alert('You have entered more Quantity that existing');
        }
        return sum + (product.quantity * product.price);
      }, 0);
    },
  },
  created() {
    this.showName = localStorage.getItem('user');
    this.retailersFromDB();
  },
  methods: {
    retailersFromDB() {
       axios
        .post(process.env.API_URL + "/retailersFromDB", {
          usertype: "Retailer",
        })
        .then(res => {
          if(res.data.numberOfretailersFromDB){
            for(var i = 0; i < res.data.numberOfretailersFromDB; i++){
              this.showRetailers.push({
                RetailerName: res.data.retailersDB[i][0],
                RetailerEmail: res.data.retailersDB[i][1]
              })
            }
          }
          else {
            this.$Message.error("No Retailers Found");
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
    displayParticularRetailerFruits(ind,retailerEmail){
      this.state = 'showFruitsState';
      axios
        .post(process.env.API_URL + "/displayParticularRetailerFruits", {
          retailerEmail: retailerEmail,
        })
        .then(res => {
          if(res.data.numberOfParticularRetailerFruitsFromDB){
            for(var i = 0; i < res.data.numberOfParticularRetailerFruitsFromDB; i++){
              this.products.push({
                retailer_Email: res.data.particularRetailerFruits[i][0],
                name: res.data.particularRetailerFruits[i][1],
                quantity1: res.data.particularRetailerFruits[i][2],
                quantity: 0,
                price: res.data.particularRetailerFruits[i][3],
              })
            }
          } else {
            this.$Message.error("No Fruits Found");
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
    storeCustomerClickedItems(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail){
      if (Cust_FruitQuantity !== 0 && Cust_FruitEnteredQuantity !== 0) {
        // console.log(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
        if (this.customerClickedItemsToStoreInDb.length === 0) {
          this.FruitCount++;
          this.customerClickedItemsToStoreInDb.push({
            Cust_FruitName: Cust_FruitName,
            Cust_FruitQuantity: Cust_FruitQuantity,
            Cust_FruitPrice: Cust_FruitPrice,
            Cust_FruitEnteredQuantity: Cust_FruitEnteredQuantity,
            Cust_ClickedSellerEmail: Cust_ClickedSellerEmail
          });
        } else {
          let notThere;
          for ( var i = 0; i < this.customerClickedItemsToStoreInDb.length; i++ ) {
            if (
              this.customerClickedItemsToStoreInDb[i].Cust_FruitName ===
                Cust_FruitName &&
              this.customerClickedItemsToStoreInDb[i]
                .Cust_ClickedSellerEmail === Cust_ClickedSellerEmail
            ) {
              this.customerClickedItemsToStoreInDb[
                i
              ].Cust_FruitEnteredQuantity = Cust_FruitEnteredQuantity;
              notThere = 0;
              break;
            }
            notThere = 1;
          }
          if (notThere) {
            this.FruitCount++;
            this.customerClickedItemsToStoreInDb.push({
              Cust_FruitName: Cust_FruitName,
              Cust_FruitQuantity: Cust_FruitQuantity,
              Cust_FruitPrice: Cust_FruitPrice,
              Cust_FruitEnteredQuantity: Cust_FruitEnteredQuantity,
              Cust_ClickedSellerEmail: Cust_ClickedSellerEmail
            });
          }
          Cust_FruitEnteredQuantity = "";
        }
      } else if(Cust_FruitEnteredQuantity ===0) {
        this.FruitCount--;
        console.log(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
        for ( var i = 0; i < this.customerClickedItemsToStoreInDb.length; i++ ) {
            if (
              this.customerClickedItemsToStoreInDb[i].Cust_FruitName ===
                Cust_FruitName &&
              this.customerClickedItemsToStoreInDb[i]
                .Cust_ClickedSellerEmail === Cust_ClickedSellerEmail
            ) {
              // this.customerClickedItemsToStoreInDb[i].Cust_FruitEnteredQuantity = Cust_FruitEnteredQuantity;
              this.customerClickedItemsToStoreInDb.splice(i,1);
              break;
            }
          }
      }
      console.log(this.customerClickedItemsToStoreInDb);
    },
    changeState(newState) {
      this.state = newState;
      this.products = [];
    },
    isNumber(evt) {
      this.evt = evt || window.event;
      const charCode = evt.which ? evt.which : evt.keyCode;
      if (charCode > 31 && (charCode < 48 || charCode > 57)) { evt.preventDefault(); }
      return true;
    },
    logout() {
      return new Promise(() => {
        // context.commit('authLogout');
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        localStorage.removeItem('status');
        this.$router.push('/');
        delete axios.defaults.headers.common.Authorization;
        // resolve();
      });
    },
    show() {
      this.$modal.show('hello-world');
    },
  },
};
</script>
<style scoped>
.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 10px 5px;
  transition: 0.2s;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 95;
}
* {
  margin: 0;
  padding: 0;
}
table {
  width: 80%;
}

#checkout {
  float: right;
  width: 40%;
  border: none;
  border-radius: 3px;
  margin: auto 0;
  padding: 0.5rem 0.75rem;
  flex-shrink: 0;
  cursor: pointer;
  /*font-size: .9rem;*/
  font-size: 20px;
  letter-spacing: 0.5px;
  transition: all 0.1s ease-in;
  background: rgb(189, 73, 73);
  color: #fff;
}
.modal-body {
  position: relative;
  padding: 20px 10px;
}

input {
  margin: 0 0.5rem 0;
  width: 35%;
  border-radius: 3px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #f1f5f8;
  color: #606f7b;
  padding: 0.5rem 0.75rem;
  box-sizing: border-box;
  font-size: 1.3rem;
  letter-spacing: 0.5px;
  margin: 0.5rem 0;
}
#secondDivision {
  color: rgb(14, 15, 15);
  float: right;
}
#list {
  list-style: none;
  color: #5e5b64;
  font-size: 20px;
  font-weight: bold;
  text-align: left;
  margin: 20px 0 15px;
  background: #fff;
  padding: 2rem;
  margin: 1rem;
  border-radius: 3px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.12), 0 2px 4px 0 rgba(0, 0, 0, 0.08);
  width: 55%;
  height: 85%;
}
#productdisplay {
  color: rgb(23, 50, 75);
}
h1,
h2 {
  color: #fff;
  font-size: 34px;
  font-family: "Cookie", cursive;
  font-weight: normal;
  line-height: 1;
  text-shadow: 0 3px 0 rgba(0, 0, 0, 0.1);
}
.btn {
  width: 20%;
  border: none;
  border-radius: 3px;
  margin: auto 0;
  padding: 0.5rem 0.75rem;
  flex-shrink: 0;
  cursor: pointer;
  /*font-size: .9rem;*/
  font-size: 20px;
  letter-spacing: 0.5px;
  transition: all 0.1s ease-in;
}

.btn[disabled] {
  background: #8795a1;
}

.btn[disabled]:hover {
  background: #606f7b;
}

.btn-primary {
  background: #6cb2eb;
  color: #fff;
}

.btn-primary:hover {
  background: #3490dc;
}

#items-list {
  align-self: auto;
  color: #fff;
  font-size: 64px;
  font-family: "Cookie", cursive;
  font-weight: normal;
  line-height: 1;
  text-shadow: 0 3px 0 rgba(0, 0, 0, 0.1);
  background-color: #61a1bc;
  border-radius: 2px;
  box-shadow: 0 1px 1px #ccc;
  width: 800px;
  padding: 35px 60px;
  margin: 50px auto;
  font: 15px/1.3 "Open Sans", sans-serif;
  color: #5e5b64;
  text-align: center;
}
</style>

