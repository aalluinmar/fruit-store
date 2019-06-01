<template>
  <div id="shopping-list">
    <h1 style="float:right">{{email}}</h1><br><br><br>
    <router-link to="/" style="float:right">Logout</router-link>
    <br>
    <div class="header">
      <h1>{{ header.toLocaleUpperCase() }}</h1>
      <br><button
        v-if="state === 'default'"
        style="float:right"
        class="btn btn-primary"
        @click="changeState('showAddItems')"
      >Add Item</button>
      <button v-else class="btn btn-cancel" @click="changeState('default')">Cancel Adding Item</button>
    </div>
    <form id="app" action method="POST" v-on:submit.prevent="adding" novalidate="true">
      <div v-if="state === 'showAddItems'" class="add-item-form">
        <input
          v-model="fruit"
          type="text"
          placeholder="Enter Fruit"
          onkeypress="return (event.charCode > 64 &&
          event.charCode < 91) || (event.charCode > 96 && event.charCode < 123)"
          style="color:blue"
        >
        <br>
        <br>
        <input
          v-model="quantity"
          type="text"
          placeholder="Enter Quantity"
          v-on:keypress="isNumber($event)"
          style="color:blue"
        >
        <input
          v-model="price"
          type="text"
          placeholder="Enter Price"
          v-on:keypress="isAnyNumber($event)"
          style="color:blue"
        >
        <button
          type="submit"
          class="btn btn-primary"
          v-if="fruit.length > 0 && quantity > 0 && price > 0"
        >Save Item</button>
      </div>
    </form>
    <button type="submit" class="btn btn-cancel" @click="displayfruits">Show Fruits</button>
    <!-- <p  v-if="items.length===0">No Fruits Available</p> -->
    <br>
    <br>
    <ul v-for="(item,index) in reversedItems" :key="index">
      <center>
        <div id="added-fruits">
          <li
            :class="{strikeout: item.purchased}"
            @click="togglePurchased(item)"
            style="color:#22292F"
          >Fruit Name: {{ item.label }}</li>
          <li style="color:#22292F">
            Fruit Quantity:
            <p style>{{item.label1}}</p>
          </li>
          <li style="color: #22292F">Fruit Price: {{item.label2}}</li>
          <li>
            <button
              class="qty btn-primary"
              v-if="state1 === 'default1'"
              @click="changeState('update')"
            >Update Quantity</button>
          </li>
          <br>
          <div v-if="state === 'update'">
            <input
              type="text"
              id="update"
              placeholder="Update Quantity"
              v-on:keypress="isNumber($event)"
              @keyup="quan = $event.target.value"
              style="color:blue"
            >
            <button class="qty btn-primary" @click="update(index,item.label)">Update</button>
          </div>
          <li>
            <button
              class="qty btn-primary"
              v-if="state2 === 'default2'"
              @click="changeState('updateprice')"
            >Update Price</button>
          </li>
          <div v-if="state === 'updateprice'">
            <input
              type="text"
              id="updateprice"
              placeholder="Update Price"
              v-on:keypress="isAnyNumber($event)"
              @keyup="pass1 = $event.target.value"
              style="color:blue"
            >
            <button class="qty btn-primary" @click="updateprice(index,item.label)">Update</button>
          </div>
        </div>
      </center>
    </ul>
    <!-- <p v-if="items.length === 0">No Fruits in Your Account.</p> -->
  </div>
</template>
<script>
import axios from "axios";
// import router from '../router';
/* eslint-disable */
export default {
  data() {
    return {
      state: "default",
      state1: "default1",
      state2: "default2",
      header: "Welcome to the Store",
      email: "neeru@gmail.com",
      usertype:"Seller",
      fruit: "",
      Fruit: "",
      Quantity: null,
      Price: null,
      quantity: null,
      price: null,
      rows: null,
      items: [],
      items1: []
    };
  },
  created() {
    // this.get_fruits()
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
    async get_fruits() {
      await axios
        .post(process.env.API_URL+"/fetchingfruits", {
          email:this.email,
          usertype:this.usertype
        })
        .then(res => {
          var numberOfRows = res.data.result.numberOfRows;
          console.log(res.data.result);
          console.log(numberOfRows);
          this.rows = numberOfRows;
          // this.items.push({
          //   label: res.data.result.
          // })
          this.items1 = res.data.result.fruitDetails;
          console.log(this.items1);
        })
        .catch(err => {
          console.log("neeraja");
        });
    },
    async displayfruits() {
      await this.get_fruits();
      this.items = [];
      for (var i = 0; i < this.items1.length; i++) {
        this.items.push({
          label: this.items1[i][0],
          label1: this.items1[i][1],
          label2: this.items1[i][2]
        });
      }
      console.log(this.items1);
    },
    adding() {
      var that = this;
      axios
        .post(process.env.API_URL+"/adding", {
          email:this.email,
          usertype:this.usertype,
          fruit: this.fruit,
          quantity: this.quantity,
          price: this.price
        })
        .then(res => {
          console.log(res);
          console.log(res.data.result);
          if (res.data.result === 0) {
            alert("fruit already exists");
          }
          else
             alert("fruit added succesfully");
          that.displayfruits()
          that.changeState("default")
          
          // this.email = "";
          // this.usertype = "";
          // this.fruit = "";
          // this.quantity = "";
          // this.price = "";
          // this.state = "default";
        })
        .catch(err => {
          console.log("error");
        });
        // this.displayfruits();
    },
    // updateQuantity(index, Quan, fruitName){
       
    // },
    update(ind, lab) {
      const temp = this.quan;
      this.lab = lab.toString();
      if (this.items[ind].label === lab) {
            axios
              .post(process.env.API_URL+"/updatingQuantity",{
                fruit: this.lab,
                quantity: this.quan,
              })
              .then(res => {
                return true;
              })
              .catch(err => {
                console.log("error");
              });
            this.items[ind].label1 = temp;
        this.quan = "";
        this.state = "default1";
      }
    },
    
    updateprice(ind, lab) {
      const temp = this.pass1;
      this.lab = lab.toString();
      if (this.items[ind].label === lab) {
            axios
              .post(process.env.API_URL + "/updatingPrice",{
                fruit: this.lab,
                price: this.pass1,
              })
              .then(res => {
                return true;
              })
              .catch(err => {
                console.log("error");
              });
             this.items[ind].label2 = temp;
        this.pass1 = "";
        this.state = "default2";
      }
    },
   
    saveItem() {
      this.items.push({
        label: this.fruit,
        label1: this.quantity,
        label2: this.price,
        purchased: false
      });
      this.fruit = "";
      this.quantity = null;
      this.price = null;
      // this.state = "default";
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
      this.fruit = "";
      this.quantity ="";
      this.price ="";
    },
    togglePurchased(item) {
      this.item.purchased = !item.purchased;
    }
  }
};
</script>
<style scoped>
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
  border: 1px solid #f1f5f8;
  color: #606f7b;
  padding: 0.5rem 0.75rem;
  box-sizing: border-box;
  font-size: 1.3rem;
  letter-spacing: 0.5px;
  margin: 0.5rem 0;
}
.add-item-form,
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.qty {
  width: 30%;
  border: none;
  border-radius: 3px;
  margin: auto 0;
  padding: 0.5rem 0.75rem;
}
input {
  background-color: cornsilk;
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
  font-size: 1.25rem;
  cursor: pointer;
  transition: all 0.1s ease-in;
}

li:hover {
  color: #22292f;
}

li input {
  margin: 0 0.5rem 0;
}
#shopping-list {
  background: #e68c8c;
  padding: 2rem;
  margin: 1rem;
  border-radius: 3px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.12), 0 2px 4px 0 rgba(0, 0, 0, 0.08);
  width: 92%;
  height: 85%;
  /*max-width: 900px;*/
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
.add-item-form,
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.add-item-form input {
  width: 70%;
  border-radius: 3px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #f1f5f8;
  color: #606f7b;
  padding: 0.5rem 0.75rem;
  box-sizing: border-box;
  font-size: 1rem;
  letter-spacing: 0.5px;
  margin: 0.5rem 0;
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
</style>
