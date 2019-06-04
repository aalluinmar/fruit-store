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
          <p class="navbar-brand" href="#">FRUIT STORE</p>
          <a>{{showName}}</a>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav navbar-right">
            <li>
              <a>Home</a>
            </li>
            <li>
              <a @click.prevent="addFruits = true">Add Items</a>
            </li>
            <li>
              <a>Transactions</a>
            </li>
            <li>
              <a style="float:right;font-size:135%;" @click="logout">Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <br>
    <br>
    <br>
    <br>
    <br>
    <center><h2><br>Fruits Details</h2></center>
    <div v-if="addFruits">
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <button type="button" class="close" @click="addFruits=false">
                    <span aria-hidden="true">&times;</span>
                  </button>
                  <h4 class="modal-title">
                    <center>Add Items</center>
                  </h4>
                </div>
                <div class="modal-body">
                  <div>
                    <center>
                      <Input
                        prefix="ios-basket"
                        placeholder="Enter Fruit"
                        size="large"
                        v-model="newItem"
                        onkeypress="return (event.charCode > 64 &&
                                event.charCode < 91) || (event.charCode > 96 &&
                                event.charCode < 123)"
                        style="width: auto"
                      />
                      <br>
                      <br>
                      <Input
                        prefix="ios-basket"
                        placeholder="Enter QUantity"
                        size="large"
                        v-on:keypress="isNumber($event)"
                        v-model="newItem1"
                        style="width: auto"
                      />
                      <br>
                      <br>
                      <Input
                        prefix="ios-basket"
                        placeholder="Enter Price"
                        size="large"
                        v-on:keypress="isAnyNumber($event)"
                        v-model="newItem2"
                        style="width: auto"
                      />
                      <br>
                      <br>
                      <button
                        type="submit"
                        class="btn btn-primary"
                        v-if="newItem.length > 0 &&newItem1 > 0 && newItem2 > 0"
                        @click="saveItem"
                      >Save Item</button>
                    </center>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
    <div>
      <ul v-for="(item,index) in reversedItems" :key="index">
        <center>
          <div id="added-fruits">
            <li
              style="color:#22292F"
            >Fruit Name: {{ item.label }}</li>
            <li style="color:#22292F">
              Fruit Quantity:
              <p style>{{item.label1}}</p>
            </li>
            <li style="color: #22292F">Fruit Price: {{item.label2}}</li>
            <li>
              <Button
                type="primary"
                @click="UpdateQuantityBoolean = true,DisplayFruit = item.label,FruitIndex = index"
              >Update Quantity</Button>
              <div v-if="UpdateQuantityBoolean">
                <transition name="modal">
                  <div class="modal-mask">
                    <div class="modal-wrapper">
                      <div class="modal-dialog">
                        <div class="modal-content">
                          <div class="modal-header">
                            <button type="button" class="close"
                            @click="UpdateQuantityBoolean = false">
                              <span aria-hidden="true">&times;</span>
                            </button>
                            <h4 class="modal-title">
                              <center>Update Quantity</center>
                            </h4>
                          </div>
                          <div class="modal-body">
                            <div>
                              <center>
                               <div>
                                 <h3 id="fruitNameDisplayOnModal">Fruit Name:  {{ DisplayFruit }}
                                 </h3>
                                 <br>
                                  <input
                                    type="text"
                                    id="update"
                                    placeholder="Update Quantity"
                                    @keyup="quan = $event.target.value"
                                    style="color:blue"
                                  >
                                  <!-- <Input prefix="ios-basket"
                                  placeholder="Update QUantity" size="large"
                                  @keyup="email = $event.target.value" style="width: auto" />-->
                                  <!-- <button class="qty btn-primary"
                                  @click="update(index,item.label)">Update</button>-->
                                  <!-- &nbsp; -->
                                  <Button type="info"
                                  @click="update(FruitIndex,DisplayFruit)">Update</Button>
                                </div>
                              </center>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </transition>
              </div>
            </li>
            <br>
            <li>
              <Button
                type="primary"
                @click="UpdatePriceBoolean = true,DisplayFruit = item.label,FruitIndex = index"
              >Update Price</Button>
              <div v-if="UpdatePriceBoolean">
                <transition name="modal">
                  <div class="modal-mask">
                    <div class="modal-wrapper">
                      <div class="modal-dialog">
                        <div class="modal-content">
                          <div class="modal-header">
                            <button type="button" class="close"
                            @click="UpdatePriceBoolean = false">
                              <span aria-hidden="true">&times;</span>
                            </button>
                            <h4 class="modal-title">
                              <center>Update Price</center>
                            </h4>
                          </div>
                          <div class="modal-body">
                            <div>
                              <center>
                               <div>
                                 <h3 id="fruitNameDisplayOnModal">Fruit Name:  {{ DisplayFruit }}
                                 </h3>
                                 <br>
                                  <input
                                    type="text"
                                    id="updateprice"
                                    placeholder="Update Price"
                                    @keyup="pass1 = $event.target.value"
                                    style="color:blue"
                                  >
                                  <!-- <button class="qty btn-primary"
                                  @click="updateprice(index,item.label)">Update</button>-->
                                  <Button type="info"
                                  @click="updateprice(FruitIndex,DisplayFruit)">Update</Button>
                                </div>
                              </center>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </transition>
              </div>
            </li>
            <li style="float:right;" id="deleteIconHover">
              <Icon type="ios-trash" size="30"
              @click="deleteParticularFruitFromSeller(item.label,index)"/>
            </li>
            <br>
          </div>
        </center>
      </ul>
    </div>
    <br>
    <center>
      <br>
      <br>
      <br>
      <h3
        v-if="items.length === 0"
        style="text-align:
      center;color:#e25f13;"
      >Oops!! No Fruits in Your Account.</h3>
    </center>
    <footer class="container-fluid text-center" id="footer">
      <br>
      <center id="footer_text">© Copyright Agency 2019.</center>
      <br>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

/* eslint-disable */
export default {
  data() {
    return {
      state: "default",
      state1: "default1",
      state2: "default2",
      header: "Welcome to the Store",
      UpdateQuantityBoolean: false,
      UpdatePriceBoolean: false,
      FruitIndex: null,
      newItem: "",
      showName: "",
      newItem1: null,
      loading: true,
      DisplayFruit: '',
      newItem2: null,
      items: [],
      addFruits: false,
      fixed: ""
    };
  },
  created() {
    this.showName = localStorage.getItem("user");
    this.showAllFruits();
  },
  computed: {
    // characterCount(){
    //     return this.newItem.length;
    // },
    reversedItems() {
      return this.items.slice(0);
    }
  },
  methods: {
    async deleteParticularFruitFromSeller(FruitName,ind){
      await this.updateSellerFruit(FruitName,"delete",ind);
      this.showAllFruits();
      this.items = [];
      
    },
    async showAllFruits(){
      await axios
        .post(process.env.API_URL + "/showAllFruits", {
          sellerEmail: this.showName,
        })
        .then(res => {
          if(res.data.numberOfFruitsFromDB === 0){
            this.$Message.error("res.data.result");
          } else {
            for(var i = 0; i < res.data.numberOfFruitsFromDB; i++){
              this.items.push({
                label: res.data.FruitsFromDB[i][1],
                label1: res.data.FruitsFromDB[i][2],
                label2: res.data.FruitsFromDB[i][3],
              })
            }
          }
        })
        .catch(err => {
          console.log(err);
          console.log('error');
        });
    },
    async addFruitsToDb(fruitName, quantity, price) {
      await axios
        .post(process.env.API_URL + "/addFruitsToDb", {
          fruitName: fruitName,
          quantity: quantity,
          price: price,
          sellerEmail: this.showName,
        })
        .then(res => {
          if(res.data.result === "Fruit already exists!"){
            this.$Message.error(res.data.result);
          } else {
            this.$Message.success("Fruit Added Successfully");
          }
        })
        .catch(err => {
          console.log(err);
          console.log('error');
        });
        this.items = [];
        this.showAllFruits();
    },
    async updateSellerFruit(FruitName,whichType,enteredThing){
      await axios
        .post(process.env.API_URL + "/updateSellerFruit", {
          fruitName: FruitName,
          whichType: whichType,
          enteredThing: enteredThing,
          sellerEmail: this.showName,
        })
        .then(res => {
          if(res.data.result === "quantity updated"){
            this.$Message.success("Updated Quantity Successfully");
          }
          else if(res.data.result === "price updated"){
            this.$Message.success("Updated Price Successfully");
          } else {
            this.$Message.success("Deleted Fruit Successfully");
          }
        })
        .catch(err => {
          console.log(err);
          console.log('error');
        });
        // this.items = [];
        // this.showAllFruits();
    },
    update(ind, lab) {
      const temp = this.quan;
      // console.log(temp, ind);
      this.lab = lab.toString();
      // console.log(this.quan);
      //   console.log(this.items.indexOf(45, 2))
      if (this.items[ind].label === lab && temp) {
        //   console.log(this.items[0].label,ind);
        // console.log(this.items[ind].label,ind,lab,temp);
        this.updateSellerFruit(lab,"quantity",temp);
        this.items[ind].label1 = temp;
        // console.log(this.quan);
        this.quan = '';
        // console.log(this.quan);
        this.state = 'default1';
        this.UpdateQuantityBoolean = false;
        ind = null;
        // this.newit='';
        // $("#update").val("");
      } else {
        this.quan = '';
        this.$Message.error('Enter Quantity');
        this.UpdateQuantityBoolean = false;
      }
    },
    updateprice(ind, lab) {
      const temp = this.pass1;
      this.lab = lab.toString();
      //   console.log(this.items.indexOf(45, 2))
      if (this.items[ind].label === lab && temp) {
        //   console.log(this.items[0].label,ind);
        // console.log(this.items[ind].label,ind,lab,temp);
        this.updateSellerFruit(lab,"price",temp);
        this.items[ind].label2 = temp;
        this.pass1 = '';
        // console.log(this.pass1);
        this.state = 'default2';
        this.UpdatePriceBoolean = false;
        // console.log(this.pass1);
        // $("#updateprice").val("");
      } else {
        this.pass1 = '';
        this.$Message.error('Enter Price');
        this.UpdatePriceBoolean = false;
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
    saveItem() {
      this.addFruitsToDb(this.newItem, this.newItem1, this.newItem2);
      this.newItem = '';
      this.newItem1 = null;
      this.newItem2 = null;
      this.addFruits = false;
    },
    isNumber(evt) {
      this.evt = evt || window.event;
      const charCode = evt.which ? evt.which : evt.keyCode;
      if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        evt.preventDefault();
      }
      return true;
    },
    isAnyNumber(evt) {
      this.evt = evt || window.event;
      const charCode = evt.which ? evt.which : evt.keyCode;
      if (
        charCode > 31 &&
        (charCode < 48 || charCode > 57) &&
        charCode !== 46
      ) {
        evt.preventDefault();
      } else {
        return true;
      }
      return 0;
    },
    changeState(newState) {
      this.state = newState;
      this.newItem = '';
    },
    // togglePurchased(item) {
    //   this.item.purchased = !item.purchased;
    // },
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
#footer {
  background-color: #333;
  position: fixed;
  bottom: 0;
  width: 10%;
  padding: -2.5rem;
  text-align: center;
}
#deleteIconHover:hover{
  transform:scale(2);
}
#footer_text {
  color: white;
}
#fruitNameDisplayOnModal{
  color: #22292f;
}
body {
  background: #eff8ff;
  height: 100vh;
  width: 98vw;
  font-family: system-ui, BlinkMacSystemFont, -apple-system, Segoe UI, Roboto,
    Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  padding: 0;
}
#update,
#updateprice {
  margin: 0 0.5rem 0;
  width: 35%;
  border-radius: 3px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border: 3px solid #f6f8f1;
  color: #606f7b;
  padding: 0.5rem 0.75rem;
  box-sizing: border-box;
  font-size: 1.3rem;
  letter-spacing: 0.5px;
  margin: 0.5rem 0;
}
/* .add-item-form,
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
} */
.qty {
  width: 30%;
  border: none;
  border-radius: 3px;
  margin: auto 0;
  padding: 0.5rem 0.75rem;
}
h1 {
  color: #3d4852;
}

ul {
  list-style: none;
  padding: 0;
}

a {
  color: #6cb2eb;
  font-size: 1.25rem;
  transition: all 0.1s ease-in;
  margin-top: 0.5rem;
  display: block;
}

a:hover {
  color: #3490dc;
}

li,
p {
  display: flex;
  align-items: center;
  line-height: 1.75;
  letter-spacing: 0.5px;
  color: #3d4852;
  font-size: 1.55rem;
  cursor: pointer;
  transition: all 0.1s ease-in;
}

li:hover {
  color: #22292f;
}

li input {
  margin: 0 0.5rem 0;
}

#added-fruits {
  background: #fff;
  padding: 2rem;
  margin: 1rem;
  border-radius: 3px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.12), 0 2px 4px 0 rgba(0, 0, 0, 0.08);
  width: 45%;
  height: 35%;
  /*max-width: 900px;*/
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

.btn-cancel {
  width: 30%;
  background: #ef5753;
  color: #fff;
}

.btn-cancel:hover {
  background: #e3342f;
  color: #fff;
}

.strikeout {
  text-decoration: line-through;
  color: #b8c2cc;
}

.strikeout:hover {
  color: #8795a1;
}
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
</style>
