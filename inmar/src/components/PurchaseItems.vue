<template>
  <div id="items-list">
    <!-- <router-link to="/" style="float:right;color:white;">Logout</router-link> -->
    <a style="float:right;font-size:135%;" @click="logout">Logout</a>
    <br>
    <h1 style="float:right">{{email}}</h1>
    <br>
    <br>
    <br>
    <!-- <h2>Total Price:{{ totalProducts}}</h2> -->

    <h1>Fruit Store Welcomes You!!</h1>
    <br>
    <button
      v-if="state === 'default'"
      type="submit"
      class="btn btn-cancel"
      @click="displayallretailers"
    >ShowRetailers</button>
    <button v-else class="btn btn-cancel" @click="changeState('default')">Cancel</button>
    <br>
    <div class="grid-container">
      <div>
        <h4 v-for="(retailer,index) in retailer1" :key="retailer.name">
          <table border="0">
            <tr>
              <td>
                <div id>
                  <h4 id="productdisplay">Name: {{retailer.retailerName}}</h4>
                  <button
                    type="submit"
                    class="btn btn-cancel"
                    @click="displayallfruits(index,retailer.retailerName)"
                  >Show Fruits</button>
                  <br>
                  <div v-if="retailer.retailerName === checkRetailerEmail">
                    <h5 v-if="fruitState">
                      <h4 v-for="product in products" :key="product.name">
                        <table border="0">
                          <tr>
                            <td>
                              <div
                                id="list"
                                @click="customerClickedItems($event, product.label, product.label1, product.label2, product.label3, retailer.retailerName)"
                              >
                                <h4 id="productdisplay">FruitName: {{product.label}}</h4>
                                <h4 id="productdisplay">Quantity: {{product.label1}}</h4>
                                <h4 id="productdisplay">Rs: {{product.label2}}</h4>

                                <input
                                  type="button"
                                  id="bt1"
                                  @click="product.label3 = (product.label3 + 1 )"
                                  value="+"
                                  class="btn btn-primary"
                                  :disabled="product.label1 <= product.label3 || product.label1 ===0"
                                >
                                <input
                                  type="text"
                                  id="qty"
                                  v-on:keypress="isNumber($event)"
                                  style="color:blue"
                                  value="0"
                                  name="quantity"
                                  v-model.number="product.label3"
                                  :disabled="product.label1 <= product.label3 || product.label1 ===0"
                                >
                                <input
                                  type="button"
                                  id="bt2"
                                  @click="product.label3 = (product.label3 - 1 )"
                                  class="btn btn-primary"
                                  value="-"
                                  :disabled="product.label3 <= 0 || product.label1 ===0"
                                >
                                <br>
                                <span v-if="product.label1 === 0" style="color:red">OUT OF STOCK</span>
                              </div>
                            </td>
                          </tr>
                        </table>
                      </h4>
                    </h5>
                  </div>
                </div>
              </td>
            </tr>
          </table>
        </h4>
      </div>
      <div>
        <h1>Here ur collection of fruits</h1>
        <h4>PRODUCTS SUMMARY</h4>
        <h4 v-for="product in customerClickedItemsToStoreInDb" :key="product.name">
          <table>
            <tr>
              <td id="secondDivision" v-if="product.Cust_FruitEnteredQuantity > 0">
                <h1>{{product.Cust_ClickedSellerEmail}}</h1>
                <h4>{{product.Cust_FruitName}}</h4>
                <p>{{product.Cust_FruitEnteredQuantity}} x Rs {{product.Cust_FruitPrice}} = Rs {{product.Cust_FruitEnteredQuantity*product.Cust_FruitPrice}}</p>
              </td>
            </tr>
          </table>
        </h4>
      </div>
    </div>

    <h2 style="text-align:right;">Total Price:{{ totalProducts}}</h2>
    <br>
    <button v-if="totalProducts > 0" id="checkout" @click="show">Check Out Rs {{totalProducts}}</button>
    <br>
    <modal name="hello-world" :width="400" :height="100">
      <h3>Fruits will be delivered within 24 Hours</h3>
      <br>
      <br>
      <h4>Thanks For Purchasing... Have a nice day</h4>
    </modal>
  </div>
</template>

<script>
import axios from "axios";
// const i = 1;
/* eslint-disable */
// module.exports = {
export default {
  data() {
    return {
      state: "default",
      email: "",
      usertype: "Seller",
      fruitState: "",
      quantity: 0,
      products: [],
      retailerName: "",
      checkRetailerEmail: "",
      products2: [],
      customerClickedItemsToStoreInDb: [],
      customerClickedItemsToStoreInDb2: [],
      retailerFromDb: [],
      Cust_FruitName: "",
      Cust_FruitQuantity: "",
      Cust_FruitPrice: "",
      Cust_FruitEnteredQuantity: "",
      Cust_ClickedSellerEmail: "",
      retailer1: []
    };
  },
  created() {
    this.email = localStorage.getItem('user');
    this.displayallretailers();
  },
  computed: {
    totalProducts() {
      return this.customerClickedItemsToStoreInDb.reduce((sum, product) => {
        if (product.Cust_FruitQuantity < product.Cust_FruitEnteredQuantity) {
          this.product.Cust_FruitEnteredQuantity = product.Cust_FruitQuantity;
          this.alert("You have entered more Quantity that existing");
        }
        return (
          sum + product.Cust_FruitEnteredQuantity * product.Cust_FruitPrice
        );
      }, 0);
    }
  },
  reversedItems() {
    return this.products.slice(0);
  },


  methods: {
    isNumber($evt) {
      this.evt = evt || window.event;
      const charCode = evt.which ? evt.which : evt.keyCode;
      if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        evt.preventDefault();
      }
      return true;
    },
    async show() {
      // this.$modal.show("hello-world");
      // this.email = email;
        await axios
        .post(process.env.API_URL + "/storingshoppingdetails", {
          // email: email,
          customerClickedDetails: this.customerClickedItemsToStoreInDb,
          customerClickedDetailsSize: this.customerClickedItemsToStoreInDb.length,
          customerEmail: this.email,
        })
        .then(res => {
           var numberOfRows = res.data.result.numberOfRows;
           this.rows = numberOfRows;
           this.customerClickedItemsToStoreInDb2 = res.data.result.fruitDetails;
          console.log(res);
          console.log(res.data.result);
          if (res.data.result === 0) {
            alert("NOT added to db");
          }
          else
             alert(" Thanks for Purchasing.........Have a nice day......Enjoy");
        })
        .catch(err => {
          console.log("neeraja");
        });
      this.displayallretailers();
      this.customerClickedItemsToStoreInDb = [];
      // console.log(this.customerClickedItemsToStoreInDb);
    },
    async get_fruits(retailername) {
      this.checkRetailerEmail = retailername;
      await axios
        .post(process.env.API_URL + "/fetchingallfruits", {
          email: retailername,
          usertype: this.usertype
        })
        .then(res => {
          var numberOfRows = res.data.result.numberOfRows;
          this.rows = numberOfRows;
          this.products1 = res.data.result.fruitDetails;
        })
        .catch(err => {
          console.log("neeraja");
        });
    },
    customerClickedItems(
      $event,
      Cust_FruitName,
      Cust_FruitQuantity,
      Cust_FruitPrice,
      Cust_FruitEnteredQuantity,
      Cust_ClickedSellerEmail
    ) {
      if (Cust_FruitQuantity !== 0 && Cust_FruitEnteredQuantity !== 0) {
        // console.log(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
        if (this.customerClickedItemsToStoreInDb.length === 0) {
          this.customerClickedItemsToStoreInDb.push({
            Cust_FruitName: Cust_FruitName,
            Cust_FruitQuantity: Cust_FruitQuantity,
            Cust_FruitPrice: Cust_FruitPrice,
            Cust_FruitEnteredQuantity: Cust_FruitEnteredQuantity,
            Cust_ClickedSellerEmail: Cust_ClickedSellerEmail
          });
        } else {
          let notThere;
          for (
            var i = 0;
            i < this.customerClickedItemsToStoreInDb.length;
            i++
          ) {
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
        console.log(this.customerClickedItemsToStoreInDb);
      } else if(Cust_FruitEnteredQuantity ===0) {
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

    },
    async displayallfruits(ind, retailername) {
      this.retailername = retailername.toString();
      await this.get_fruits(retailername);
      this.fruitState = true;
      this.products = [];
      for (var i = 0; i < this.products1.length; i++) {
        this.products.push({
          label: this.products1[i][0],
          label1: this.products1[i][1],
          label2: this.products1[i][2],
          label3: this.quantity
        });
      }
    },
    async displayallretailers() {
      await axios
        .post(process.env.API_URL + "/fetchingallretailers", {
          usertype: this.usertype
        })
        .then(res => {
          var numberOfRows = res.data.result.numberOfRows;
          this.rows = numberOfRows;
          this.retailerFromDb = res.data.result.fruitDetails;
        })
        .catch(err => {
          console.log("error");
        });
      this.retailer1 = [];
      this.fruitState = false;
      for (var i = 0; i < this.retailerFromDb.length; i++) {
        this.retailer1.push({
          retailerName: this.retailerFromDb[i][0]
        });
      }
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
    changeState(newState) {
      this.state = newState;
    }
  }
};
</script>
/* eslint-disable */
<style scoped>
* {
  margin: 0;
  padding: 0;
}
table {
  width: 110%;
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
}
#list {
  list-style: none;
  color: #fff;
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
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  grid-gap: 10px;
  background-color: #2196f3;
  padding: 10px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 20px 0;
  font-size: 30px;
}
</style>

