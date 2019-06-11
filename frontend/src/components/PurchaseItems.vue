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
              <a @click="transactionOfCustomer = true">Transactions</a>
            </li>
            <li style="color:white">
              <a style="color:white" v-if="totalProducts !== 0">Total Price:{{ totalProducts }}</a>
            </li>
            <li>
              <a @click="showModal_checkout = true">
                <Icon type="ios-cart-outline" size="24"/>{{ FruitCount }}</a>
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
        <h4 v-for="(retailer,index) in showRetailers" :key="retailer.RetailerEmail+'email'">
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
        <h4 v-for="product in products" :key="product.name+'productName'">
          <h5 v-for="(calculatePrice,index) in customerClickedItemsToStoreInDb"
            :key="calculatePrice.Cust_FruitPrice+'custPricing'+index">
            <h6 v-if="calculatePrice.Cust_ClickedSellerEmail === product.retailer_Email
            && calculatePrice.Cust_FruitName === product.name">
            <h6 v-if="product.quantity = calculatePrice.Cust_FruitEnteredQuantity">
            </h6>
            </h6>
          </h5>
          <center>
          <table border="0">
            <tr>
              <td>
                <div id="list">
                  <h4 id="productdisplay" style="float:right;color:#5ce61c;">Retailer:
                    {{ product.retailer_Email}}</h4>
                  <h4 id="productdisplay">Fruit: {{ product.name}}</h4>
                  <h4 id="productdisplay">Quantity: {{ product.quantity1}}</h4>
                  <h4 id="productdisplay">Rs: {{ product.price}}</h4><br>
                  <ButtonGroup>
                      <Button type="primary" @click.prevent="product.quantity =
                      (product.quantity + 1 ),
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
                      <Button type="primary" @click.prevent="product.quantity =
                      (product.quantity - 1 ),
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
    <div v-if="showModal_checkout">
      <center>
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h2 class="modal-title">
                  <button type="button" class="close" @click="showModal_checkout=false">
                    <!-- <span aria-hidden="true">&times;</span> -->
                    <Icon type="md-close" />
                  </button>
                    <center>Cart List</center>
                  </h2>
                </div>
                <div class="modal-body">
                  <div>
                    <center>
                      <h3 v-if="totalProducts <= 0">No items in Your cart</h3>
                      <h3 v-else>Total Products List</h3>
                        <h5 v-for="(calculatePrice,index) in ItemsFromCart"
                          :key="calculatePrice.Cust_FruitPrice+'cusPrice'+index">
                              <Card style="width:350px">
                                <h4 style="color:#5ce61c">Retailer:
                                  {{ calculatePrice.custClickedEmail }}</h4>
                                <h4 style="float:left">Fruit :
                                  {{calculatePrice.FRUIT_name}}</h4>
                                <h4 style="float:right">Quantity:
                                  {{ calculatePrice.FRUIT_quantity }}</h4><br>
                                <h4 style="float:left;">Quantity Required:
                                  {{ calculatePrice.FRUIT_enteredQuantity }}</h4>
                                <p>
                                  <br><br>
                                  {{calculatePrice.FRUIT_enteredQuantity}} x Rs
                                  {{calculatePrice.FRUIT_price}}
                                  = Rs {{calculatePrice.FRUIT_enteredQuantity*
                                  calculatePrice.FRUIT_price}}
                                </p>
                                <Icon type="ios-trash" size="30" style="float:right;"
                                id="deleteIconHover"
                                @click="deleteParticularFruitFromCart(
                                  calculatePrice.custClickedEmail, calculatePrice.FRUIT_name
                                  ,index)"/>
                                <br><br>
                              </Card> <br>
                        </h5>
                        <br><br>
                        <h2 style="text-align:right;">Total Price:{{ totalProducts}}</h2>
                        <br>
                        <ButtonGroup size="large">
                          <Button type="primary" @click="show"
                          :disabled="totalProducts <= 0">Checkout</Button>
                        </ButtonGroup>
                    </center>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
      </center>
    </div>
    <div v-if="transactionOfCustomer">
      <center>
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h2 class="modal-title">
                  <button type="button" class="close" @click="transactionOfCustomer=false">
                    <!-- <span aria-hidden="true">&times;</span> -->
                    <Icon type="md-close" />
                  </button>
                    <center>Transaction History</center>
                  </h2>
                </div>
                <div class="modal-body">
                  <div>
                    <center>
                      <h3 v-if="totalProducts <= 0">No Transactions Upto now</h3>
                      <h3 v-else>History</h3>
                        <h5 v-for="(showTransaction,index) in showTransactions"
                          :key="index">
                              <Card style="width:400px">
                                <h4 slot="title">Transaction ID:
                                  #{{ showTransaction.transactionID }}</h4> <br>
                                <p  style="float:left">Transaction Date:
                                  {{ showTransaction.TransDate }}</p>
                                <p  style="float:right">Time:
                                  {{ showTransaction.TransTime }}</p><br>
                                    <Card>
                                      <p  style="float:left;color:black;">Retailer:
                                      {{ showTransaction.RetailerEmail }}</p><br>
                                      <p style="float:left">Fruit :
                                        {{showTransaction.fruitName}}</p>
                                      <p  style="float:right">Quantity:
                                        {{ showTransaction.Quantity }}</p>
                                      <p>Purchased Quantity:
                                        {{ showTransaction.purchasedQuantity }}</p>
                                      <p>Price:
                                        {{ showTransaction.price }}</p>
                                      <p>Total Price:
                                        {{ showTransaction.totalPrice }}</p>
                                    </Card>
                                    <!-- <h5 v-for="(checkTransId,index1) in showTransactions"
                                        :key="index1+'index1'">
                                        <h5 v-if="checkTransId.transactionID ===
                                        showTransaction.transactionID">
                                          <h5 v-if="showTransaction.fruitName !==
                                          checkTransId.fruitName">
                                          <p v-if="transactionIdexistsalready = true"></p>
                                          {{index1}}
                                          <Card>
                                            <p  style="float:left;color:black;">Retailer:
                                            {{ checkTransId.RetailerEmail }}</p><br>
                                            <p style="float:left">Fruit :
                                              {{checkTransId.fruitName}}</p>
                                            <p  style="float:right">Quantity:
                                              {{ checkTransId.Quantity }}</p>
                                            <p>Purchased Quantity:
                                              {{ checkTransId.purchasedQuantity }}</p>
                                            <p>Price:
                                              {{ checkTransId.price }}</p>
                                            <p>Total Price:
                                              {{ checkTransId.totalPrice }}</p>
                                          </Card>
                                          </h5>
                                        </h5>
                                    </h5> -->
                              </Card> <br>
                              <h5 v-if="transactionIdexistsalready">
                                <h6 v-if="index = index + 1">{{index}}</h6>
                              </h5>
                        </h5>
                        <ButtonGroup size="large">
                          <Button type="primary" @click="transactionOfCustomer=false">Close</Button>
                        </ButtonGroup>
                    </center>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
      </center>
    </div>
    <!-- <h2 style="text-align:right;">Total Price:{{ totalProducts}}</h2>
    <br> -->
    <br>
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
      showTransactions: [],
      ItemsFromCart: [],
      state: 'default',
      showFruitsBoolean : false,
      showRetailerBoolean: true,
      transactionIdexistsalready: false,
      TransDate: 0,
      TransTime: 0,
      dateTIME: 0,
      FruitCount: 0,
      showModal_checkout: false,
      transactionOfCustomer: false,
      products: [],
      customerClickedItemsToStoreInDb: [],
      transRows: 0,
    };
  },
  computed: {
    totalProducts() {
      return this.ItemsFromCart.reduce((sum, product) => {
        // if(Cust_FruitEnteredQuantity !== 0)
        if (product.FRUIT_quantity < product.FRUIT_enteredQuantity) {
          this.product.FRUIT_enteredQuantity = product.FRUIT_quantity;
          this.alert('You have entered more Quantity that existing');
        }
        return sum + (product.FRUIT_enteredQuantity * product.FRUIT_price);
      }, 0);
      this.ItemsFromCart = [];
    },
  },
  created() {
    this.showName = localStorage.getItem('user');
    this.retailersFromDB();
    this.transactionHistory();
    this.customerCartDetails();
  },
  methods: {
    async deleteParticularFruitFromCart(custClickedEmail, FRUIT_name,inde) {
      axios
        .post(process.env.API_URL + "/deleteParticularFruitFromCart", {
          retailerEmail: custClickedEmail,
          fruitName: FRUIT_name,
          customerEmail: this.showName,
        })
        .then(res => {
          console.log(res.data.particularCustomerCart);
          if(res.data.particularCustomerCart){
            this.$Message.success("Fruit Deleted Successfully from Cart");
            this.storeCustomerClickedItems(FRUIT_name, null, null, 0, custClickedEmail);
            this.state = 'default';
            // this.customerCartDetails();
          }
          else {
            this.$Message.error("Fruit Not Deleted From cart");
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
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
    customerCartDetails() {
      this.ItemsFromCart = [];
      axios
        .post(process.env.API_URL + "/customerCartDetails", {
          customerEmail: this.showName,
        })
        .then(res => {
          this.FruitCount = res.data.cartRows;
          if(res.data.cartRows){
            for(var i = 0; i < res.data.cartRows; i++){
              this.ItemsFromCart.push({
                custClickedEmail: res.data.cartItemsFromDB[i][0],
                FRUIT_name: res.data.cartItemsFromDB[i][2],
                FRUIT_quantity: res.data.cartItemsFromDB[i][3],
                FRUIT_price: res.data.cartItemsFromDB[i][4],
                FRUIT_enteredQuantity: res.data.cartItemsFromDB[i][5],
              })
            }
          }
          else {
            this.$Message.error("No Items In your cart");
          }
        })
        .catch(err => {
          console.log(err);
        });
        console.log(this.ItemsFromCart);
    },
    async transactionHistory() {
        await axios
        .post(process.env.API_URL + "/transactionHistory", {
          customerEmail: this.showName,
        })
        .then(res => {
          if(res.data.transactionRows){
            this.transRows = res.data.transactionRows;
            for(var i = 0; i < res.data.transactionRows; i++){
              this.dateTIME = res.data.transactionHistory[i][8];
              this.TransDate = this.dateTIME.substring(0,10).toString().split("-").reverse().join("-");
              this.TransTime = this.dateTIME.substring(11,19);
              this.showTransactions.push({
                RetailerEmail: res.data.transactionHistory[i][0],
                fruitName: res.data.transactionHistory[i][2],
                Quantity: res.data.transactionHistory[i][3],
                purchasedQuantity: res.data.transactionHistory[i][4],
                price: res.data.transactionHistory[i][5],
                totalPrice: res.data.transactionHistory[i][6],
                transactionID: res.data.transactionHistory[i][7].substring(0,14),
                TransDate: this.TransDate,
                TransTime: this.TransTime
              })
            }
            // console.log(this.showTransactions);
          }
          else {
            this.$Message.error("No Transactions Found");
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
    async storeCustomerClickedItems(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail){
      // this.ItemsFromCart = [];
      if (Cust_FruitQuantity !== 0 && Cust_FruitEnteredQuantity !== 0) {
        // console.log(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
        if (this.customerClickedItemsToStoreInDb.length === 0) {
          // this.FruitCount++;
          this.customerClickedItemsToStoreInDb.push({
            Cust_FruitName: Cust_FruitName,
            Cust_FruitQuantity: Cust_FruitQuantity,
            Cust_FruitPrice: Cust_FruitPrice,
            Cust_FruitEnteredQuantity: Cust_FruitEnteredQuantity,
            Cust_ClickedSellerEmail: Cust_ClickedSellerEmail
          });
          this.addItemsTocart(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
        } else {
          let notThere;
          for ( var i = 0; i < this.customerClickedItemsToStoreInDb.length; i++ ) {
            if (
              this.customerClickedItemsToStoreInDb[i].Cust_FruitName ===
                Cust_FruitName &&
              this.customerClickedItemsToStoreInDb[i]
                .Cust_ClickedSellerEmail === Cust_ClickedSellerEmail
            ) {
              this.customerClickedItemsToStoreInDb[i].Cust_FruitEnteredQuantity =
              Cust_FruitEnteredQuantity;
              // this.customerClickedItemsToStoreInDb[i].Cust_FruitEnteredQuantity =
              // this.customerClickedItemsToStoreInDb[i].Cust_FruitEnteredQuantity + 1;
              notThere = 0;
              await this.addItemsTocart(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
              break;
            }
            notThere = 1;
          }
          if (notThere) {
            // this.FruitCount++;
            this.customerClickedItemsToStoreInDb.push({
              Cust_FruitName: Cust_FruitName,
              Cust_FruitQuantity: Cust_FruitQuantity,
              Cust_FruitPrice: Cust_FruitPrice,
              Cust_FruitEnteredQuantity: Cust_FruitEnteredQuantity,
              Cust_ClickedSellerEmail: Cust_ClickedSellerEmail
            });
            await this.addItemsTocart(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
          }
          Cust_FruitEnteredQuantity = "";
        }
        this.$Message.success("Added to cart");
      } else if(Cust_FruitEnteredQuantity ===0) {
        // this.FruitCount--;
        console.log(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
        for ( var i = 0; i < this.customerClickedItemsToStoreInDb.length; i++ ) {
            if (
              this.customerClickedItemsToStoreInDb[i].Cust_FruitName ===
                Cust_FruitName &&
              this.customerClickedItemsToStoreInDb[i]
                .Cust_ClickedSellerEmail === Cust_ClickedSellerEmail
            ) {
              // this.customerClickedItemsToStoreInDb[i].Cust_FruitEnteredQuantity = Cust_FruitEnteredQuantity;
              await this.addItemsTocart(Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail);
              this.customerClickedItemsToStoreInDb.splice(i,1);
              this.$Message.error("Removed from cart");
              break;
            }
          }
      }
      // console.log("===",this.customerClickedItemsToStoreInDb);
    },
    async addItemsTocart(custFruitName, custQuantity, custPrice, custEnteredQuantity, custClickedEmail){
      let alreadyExists = 1;
      console.log(custFruitName, custQuantity, custPrice, custEnteredQuantity, custClickedEmail);
      await axios
        .post(process.env.API_URL + "/addItemsTocart", {
          customerEmail: this.showName,
          custFruitName: custFruitName,
          custQuantity: custQuantity,
          custPrice: custPrice,
          custEnteredQuantity: custEnteredQuantity,
          retailerEmail: custClickedEmail,
        })
        .then(res => {
          console.log(res.data.itemscartDB);
          this.ItemsFromCart = [];
          this.customerCartDetails();
          console.log(this.ItemsFromCart);
          // console.log(res.data.itemscartDB);
          // if(res.data.numberOfItemsFromCartDB){
          //     for(var j = 0; j < this.ItemsFromCart.length; j++){
          //       if(res.data.itemscartDB.retailerEmail === this.ItemsFromCart[j].custClickedEmail
          //       && res.data.itemscartDB.custFruitName === this.ItemsFromCart[j].FRUIT_name){
          //         this.ItemsFromCart[j].FRUIT_enteredQuantity = res.data.itemscartDB.custEnteredQuantity;
          //         alreadyExists = 0;
          //         break;
          //       }
          //     }
          //     if(alreadyExists){
          //       this.ItemsFromCart.push({
          //         custClickedEmail: res.data.itemscartDB.retailerEmail,
          //         FRUIT_name: res.data.itemscartDB.custFruitName,
          //         FRUIT_quantity: res.data.itemscartDB.custQuantity,
          //         FRUIT_price: res.data.itemscartDB.custPrice,
          //         FRUIT_enteredQuantity: res.data.itemscartDB.custEnteredQuantity,
          //       })
          //     }
          // } else {
          //   for(var j = 0; j < this.ItemsFromCart.length; j++){
          //       if(res.data.itemscartDB.retailerEmail === this.ItemsFromCart[j].custClickedEmail
          //       && res.data.itemscartDB.custFruitName === this.ItemsFromCart[j].FRUIT_name){
          //         // this.ItemsFromCart[j].FRUIT_enteredQuantity = res.data.itemscartDB.custEnteredQuantity;
          //         this.ItemsFromCart.splice(j,1);
          //         break;
          //       }
          //   }
          // }
        })
        .catch(err => {
          console.log("error");
          console.log(err);
        });
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
      axios
        .post(process.env.API_URL + "/customerTransaction", {
          customerClickedItemsToStoreInDb: this.customerClickedItemsToStoreInDb,
          customerEmail: this.showName,
        })
        .then(res => {
          console.log(res);
          this.showModal_checkout = false;
          this.customerClickedItemsToStoreInDb = [];
          this.transactionHistory = [];
          this.FruitCount = 0;
          this.state = 'default';
          this.ItemsFromCart = [];
          this.totalProducts;
          this.$Message.success("Thanks for Purchasing");
        })
        .catch(err => {
          console.log(err);
          this.$Message.error("Sorry for Inconvenience");
        });
        // this.transactionHistory();
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
#deleteIconHover:hover{
  transform:scale(2);
}
#productdisplay {
  color: rgb(23, 50, 75);
}
h1,
h2 {
  color: rgb(10, 1, 1);
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
.modal-body {
  position: relative;
  padding: 30px 15px;
  max-height: calc(100vh - 200px);
  overflow-y: auto;
}
.modal-header{
  width: 100%;
  height: 100%;
}
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  text-align: center;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.5s ease;
}
.modal {
  text-align: center;
  /* overflow: hidden; */
  padding: 0!important;
}
.modal:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
  margin-right: -4px;
}
.modal-dialog {
  display: inline-block;
  text-align: left;
  vertical-align: middle;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
</style>

