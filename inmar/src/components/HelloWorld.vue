<template>
  <div id="app">
    <div id="shopping-list" rows="3">
      <div class="header">
        <h1>{{ header.toLocaleUpperCase() }}</h1>
        <button
          v-if="state === 'default'"
          class="btn btn-primary"
          @click="changeState('rsignup')"
        >SignUp</button>
         <button
          v-if="state === 'default'"
          class="btn btn-primary"
          @click="changeState('rlogin')"
        >Login</button>
        
        
        
        <button v-else class="btn btn-cancel" @click="changeState('default')">Cancel</button>
      </div>

      <div v-if="state === 'rsignup'">
        <center class="add-item-form1">
          <form id="app" v-on:submit.prevent="register" 
          action method="POST" novalidate="true">
            <div class="form-group">
              <!-- <h5 v-if="errors.length" >
                      <p >
                        <h5 v-for="error in errors" style="color: red">{{ error }}</h5>
                      </p>
              </h5>-->
            </div>
            <div class="form-group">
              <label for="name">
                Name
                <sup>*</sup>
              </label>
              <br>
              <input type="text" name="name" id="name" v-model="name">
              <br>
              <span v-if="errors" id="alert">{{errors.name}}</span>
              <br>
            </div>
            <div class="form-group">
              <label for="email">
                Email
                <sup>*</sup>
              </label>
              <br>
              <input type="email" name="email" id="email" v-model="email">
              <br>
              <span v-if="errors" id="alert">{{errors.email}}</span>
              <br>
            </div>
            <div class="form-group">
              <label for="usertype">
                usertype
                <sup>*</sup>
              </label>
              <br>
              <!-- <input type="text" name="usertype" id="usertype" v-model="usertype"> -->
              <select v-model="usertype">
                <option value=""></option>
                <option value="Seller" >Seller</option>
                <option value="Buyer">Buyer</option>
              </select>
              <br>
              <span v-if="errors" id="alert">{{errors.usertype}}</span>
              <br>
            </div>
            <div class="form-group">
              <label for="password">
                Password
                <sup>*</sup> &nbsp;
                <sub>(Contains 1 special character, digit,Alphabet</sub>
              </label>
              <br>
              <input type="password" name="password" id="password" v-model="password">
              <br>
              <span v-if="errors" id="alert">{{errors.password}}</span>
              <br>
            </div>
             <button type="submit" class="btn btn-cancel">Submit</button>
            <!-- <input type="submit" value="Submit"> -->
          </form>
        </center>
      </div>


      <div v-if="state === 'rlogin'">
        <center>
          <div class="add-item-form1">
            <form id="app" v-on:submit.prevent="rlogin" action method="post" novalidate="true">
              <div class="form-group">
                <!-- <h5 v-if="errors1.length" >
                    <p>
                        <h5 v-for="error in errors1" style="color: red">{{ error }}</h5>
                    </p>
                </h5>-->
              </div>
              <div class="form-group">
                <label for="email">
                  Email
                  <sup>*</sup>
                </label>
                <br>
                <input type="email" name="email" id="email"  v-model="email">
                <br>
                <span v-if="errors1" id="alert">{{errors1.email}}</span>
                <br>
              </div>
              <div class="form-group">
              <label for="usertype">
                usertype
                <sup>*</sup>
              </label>
              <br>
              <!-- <input type="text" name="usertype" id="usertype" v-model="usertype"> -->
              <select v-model="usertype">
                <option value=""></option>
                <option value="Seller">Seller</option>
                <option value="Buyer">Buyer</option>
              </select>
              <br>
              <span v-if="errors1" id="alert">{{errors1.usertype}}</span>
              <br>
            </div>
              <div class="form-group">
                <label for="password">
                  Password
                  <sup>*</sup>
                </label>
                <br>
                <input type="password" name="password" id="password" v-model="password">
                <br>
                <span v-if="errors1" id="alert">{{errors1.password}}</span>
                <br>
              </div>
              <!-- <input type="submit" value="Submit"> -->
              <button type="submit" class="btn btn-cancel" >Submit</button>
              <!-- <button>Submit</button> -->
            </form>
          </div>
        </center>
      </div>

     
      
      

   
      <p v-if="state === 'default'">WELCOME TO FRUIT STORE</p>
      <p v-if="state === 'default'" class="fruitmatter">
        Fruit has been recognized as a good source of vitamins and
        minerals, and for their role in preventing vitamin C and vitamin A deficiencies.
        People who eat fruit as part of an overall healthy diet generally have a reduced
        risk of chronic diseases. USDA's MyPlate encourages making half your plate fruits
        and vegetables for healthy eating.
        <br>Fruit are important sources of many nutrients,
        including potassium, fiber, vitamin C and folate (folic acid).
        Try incorporating blueberries, citrus fruit, cranberries or strawberries
        which contain phytochemicals that are being studied for added health benefits.
        <br>The nutrients in fruit are vital for health and maintenance of your body.
        The potassium in fruit can reduce your risk of heart disease and stroke.
        Potassium may also reduce the risk of developing kidney stones
        and help to decrease bone loss as you age.
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import router from '../router';
/* eslint-disable */
export default {
  data() {
    return {
      state: "default",
      header: "Fruit Store",
      newItem: "",
      errors: {},
      // emailloginverify:true,
      // passloginverify:true,
      errors1: {},
      name: null,
      usertype: null,
      email: null,
      password: null,
      items: []
    };
  },
  methods: {
    register() {
      if(this.checkForm()) {
        console.log("----");
        axios.post(process.env.API_URL+"/register",{
          name: this.name,
          email: this.email,
          usertype: this.usertype,
          password: this.password
        })
        .then(res => {
          console.log(res);
          console.log(res.data.result);
          if(res.data.result === 0){
            alert("email already exixts");
            this.name="";
            this.usertype="";
            this.password="";
            this.email="";
            this.state='default';
          }
          else{
            if(this.usertype==='Seller')
              router.push({ name: "Sellitems" , params:{ id:res.data.result.email}});
            else
              router.push({ name: "PurchaseItems" , params:{ id:res.data.result.email}});
          }
        })
        .catch(err => {
          console.log("error");
        })
      }
    },
    
    rlogin() {
      if(this.checkForm1()) {
        axios.post(process.env.API_URL+"/rlogin",{
          email: this.email,
          usertype: this.usertype,
          password: this.password
        })
        .then(res => {
          console.log(res);
          if(res.data.result === "INVALID EMAIL OR USERTYPE"){
            alert(res.data.result);
            this.email="";
            this.usertype = "";
            this.password="";
            this.state='default';
          }
          else if(res.data.result === "INVALID PASSWORD"){
            alert(res.data.result);
            this.email="";
            this.usertype = "";
            this.password="";
            this.state='default';
          }
          else{
            if(this.usertype==='Seller')
              router.push({ name: "Sellitems" , params:{ id:res.data.result.email}});
            else
              router.push({ name: "PurchaseItems" , params:{ id:res.data.result.email}});

          }
        })
        .catch(err => {
          console.log("error");
        })
      }
    },
    
    changeState(newState) {
      this.state = newState;
      this.newItem = "";
    },
    // loginbutton: function(){
    //   this.$router.push('/Demo');
    // },
    checkForm(e) {
      this.errors = {};
      if(!this.usertype){
        this.errors.usertype =" User Type Required";
      }
      if (!this.name) this.errors.name = "Name required.";
      if (!this.email) {
        this.errors.email = "Email required.";
      } else if (!this.validEmail(this.email)) {
        this.errors.email = "Valid email required.";
      }
      if (!this.password) {
        this.errors.password = "Password required.";
      } else if (!this.validPassword(this.password)) {
        this.errors.password = "Valid Password required.";
      }
      if (!Object.keys(this.errors).length) {
        // this.$router.push("/Sellitems");
        return true;
      }
      // e.preventDefault();
      return false;
    },
    
    checkForm1(e) {
      this.errors1 = {};
      if(!this.usertype){
        this.errors1.usertype =" User Type Required";
      }
      if (!this.email) {
        this.errors1.email = "Email required.";
        // emailloginverify:false;
      } else if (!this.validEmail(this.email)) {
        this.errors1.email = "Valid email required.";
        // emailloginverify:false;
      }
      if (!this.password) {
        this.errors1.password = "Password required.";
        // passloginverify:false;
      } else if (!this.validPassword(this.password)) {
        this.errors1.password = "Valid Password required.";
        // passloginverify:false;
      }
      if (!Object.keys(this.errors1).length) {
        // this.$router.push("/PurchaseItems");
        return true;
      }
      // e.preventDefault();
      // // if(this.emailloginverify == this.passloginverify){

      // }
      return false;
    },
    validEmail(email) {
      const re = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    validPassword(password) {
      const re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
      return re.test(password);
    }
  }
};
</script>
<style scoped>
sup {
  color: red;
}
#alert {
  color: red;
  font-size: 100%;
}
#name,
#email,
#password {
  font-weight: bold;
  font-weight: 900;
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
.fruitmatter {
  font-family: "Comic Sans MS", cursive, sans-serif;
}
#shopping-list {
  background: #fff;
  padding: 2rem;
  margin: 1rem;
  border-radius: 3px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.12), 0 2px 4px 0 rgba(0, 0, 0, 0.08);
  width: 95%;
  height: 85%;
  /*max-width: 900px;*/
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

#shopping-list > input,
#shopping-list > select {
  width: 100%;
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
.add-item-form1 input {
  width: 50%;
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

.priority {
  color: #de751f;
}
</style>
