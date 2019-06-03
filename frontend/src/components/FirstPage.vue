<template>
  <div id="app">
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
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav">
            <li>
              <a href="/">Home</a>
            </li>
            <li>
              <a href="#about">About</a>
            </li>
            <li>
              <a href="#info">Contact</a>
            </li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li>
              <a
                class="glyphicon glyphicon-log-in"
                id="show-modal"
                @click="showModal = true"
              >SignUp</a>
            </li>
            <li>
              <a
                class="glyphicon glyphicon-log-in"
                id="show-modal"
                @click="showModalLogin = true"
              >Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <br>
    <br>
    <br>
    <br>
    <div class="row">
      <div class="col-sm-12">
        <div class="header">
          <div v-if="showModal">
            <transition name="modal">
              <div class="modal-mask">
                <div class="modal-wrapper">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <button type="button" class="close" @click="showModal=false">
                          <span aria-hidden="true">&times;</span>
                        </button>
                        <h4 class="modal-title"><center>Registration</center></h4>
                      </div>
                      <div class="modal-body">
                        <div>
                          <center>
                            <form
                              id="app"
                              v-on:submit.prevent="register"
                              action
                              method="POST"
                              novalidate="true"
                            >
                              <div class="form-group">
                                <RadioGroup v-model="usertype" type="button" size="large">
                                    <Radio label="Retailer">Retailer</Radio>
                                    <Radio label="Customer">Customer</Radio>
                                </RadioGroup>
                                <br>
                                <span v-if="errors" id="alert">{{errors.usertype}}</span>
                                <br>
                              </div>
                              <div class="form-group">
                                <label for="name">
                                  Name
                                  <sup>*</sup>
                                </label>
                                <br>
                                <Input prefix="ios-contact" placeholder="Enter name" size="large"
                                v-model="name" style="width: auto" />
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
                                <Input prefix="ios-mail" placeholder="Enter Email" size="large"
                                v-model="email" style="width: auto" />
                                <br>
                                <span v-if="errors" id="alert">{{errors.email}}</span>
                                <br>
                              </div>
                              <div class="form-group">
                                <label for="password">
                                  Password
                                  <sup>*</sup> &nbsp;
                                  <sub>(Contains 1 special character, digit,Alphabet</sub>
                                </label>
                                <br>
                                <Input prefix="ios-lock" type="password"
                                placeholder="Enter Password" size="large"
                                v-model="password" style="width: auto" />
                                <br>
                                <span v-if="errors" id="alert">{{errors.password}}</span>
                                <br>
                              </div>
                              <button type="submit" class="btn btn-cancel">Register</button>
                            </form>
                          </center>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>
          <div v-if="showModalLogin">
            <transition name="modal">
              <div class="modal-mask">
                <div class="modal-wrapper">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <button type="button" class="close" @click="showModalLogin=false">
                          <span aria-hidden="true">&times;</span>
                        </button>
                        <h4 class="modal-title"><center>Login</center></h4>
                      </div>
                      <div class="modal-body">
                        <center>
                          <div>
                            <form
                              id="app"
                              v-on:submit.prevent="Login"
                              action
                              method="post"
                              novalidate="true"
                            >
                              <div class="form-group">
                                <RadioGroup v-model="usertype" type="button" size="large">
                                    <Radio label="Retailer">Retailer</Radio>
                                    <Radio label="Customer">Customer</Radio>
                                </RadioGroup>
                                <br>
                                <span v-if="errors1" id="alert">{{errors1.usertype}}</span>
                                <br>
                              </div>
                              <div class="form-group">
                                <label for="email">
                                  Email
                                  <sup>*</sup>
                                </label>
                                <br>
                                <!-- <input type="email" name="email" id="email"
                                v-model="email"> -->
                                <Input prefix="ios-mail" placeholder="Enter Email" size="large"
                                v-model="email" style="width: auto" />
                                <br>
                                <span v-if="errors1" id="alert">{{errors1.email}}</span>
                                <br>
                              </div>
                              <div class="form-group">
                                <label for="password">
                                  Password
                                  <sup>*</sup>
                                </label>
                                <br>
                                <Input prefix="ios-lock" type="password"
                                placeholder="Enter Password" size="large"
                                v-model="password" style="width: auto" />
                                <br>
                                <span v-if="errors1" id="alert">{{errors1.password}}</span>
                                <br>
                              </div>
                              <!-- <input type="submit" value="Submit"> -->
                              <button type="submit" class="btn btn-cancel">Submit</button>
                            </form>
                          </div>
                        </center>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>

          <!-- <button id="show-modal" @click="showModal = true">Show Modal</button> -->
        </div>
      </div>
    </div> <br>
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div id="myCarousel" class="carousel slide" data-ride="carousel">
            <!-- Wrapper for slides -->
            <div class="carousel-inner" role="listbox">
              <div class="item active">
                <img src="@/assets/images/1st.jpg" alt="Image">
                <div class="carousel-caption">
                  <center data-target="#myCarousel" data-slide-to="0">
                    <h3>A Healthy outside starts from the inside</h3>
                  </center>
                </div>
              </div>

              <div class="item">
                <img src="@/assets/images/2nd.jpg" alt="Image">
                <div class="carousel-caption">
                  <center data-target="#myCarousel" data-slide-to="1">
                    <h3>You are What you eat</h3>
                  </center>
                </div>
              </div>
              <div class="item">
                <img src="@/assets/images/3rd.jpg" alt="Image">
                <div class="carousel-caption">
                  <center data-target="#myCarousel" data-slide-to="2">
                    <h3>Food is Fuel not Therapy</h3>
                  </center>
                </div>
              </div>
              <div class="item">
                <img src="@/assets/images/4th.jpg" alt="Image">
                <div class="carousel-caption">
                  <center data-target="#myCarousel" data-slide-to="3">
                    <h3>Don't eat less eat right</h3>
                  </center>
                </div>
              </div>
              <div class="item">
                <img src="@/assets/images/5th.jpg" alt="Image">
                <div class="carousel-caption">
                  <center data-target="#myCarousel" data-slide-to="4">
                    <h3>Healthy Food Healthy Life</h3>
                  </center>
                </div>
              </div>
            </div>

            <!-- Left and right controls -->
            <p class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
              <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </p>
            <p class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
              <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </p>
          </div>
        </div>
        <!-- <div class="col-sm-4">
        <div class="well">
          <p>Some text..</p>
        </div>
        <div class="well">
          <p>Upcoming Events..</p>
        </div>
        <div class="well">
          <p>Visit Our Blog</p>
        </div>
        </div>-->
      </div>
    </div>

    <div class="container text-center"><br> <br> <br>
      <h3>Use Of Fruits</h3>
      <br>
      <div class="row">
        <div class="col-sm-3">
          <!-- <img src="./assets/images/guava.jpg"> -->
          <img
            src="@/assets/images/guava.jpg"
            class="img-responsive"
            style="width:100%"
            height="50%"
            alt="Image"
          >
          <p>Best Protien Fruit</p>
        </div>
        <div class="col-sm-3">
          <img
            src="@/assets/images/lemon.jpg"
            class="img-responsive"
            style="width:100%"
            height="50%"
            alt="Image"
          >
          <p>Protect against Cancer</p>
        </div>
        <div class="col-sm-3">
          <div class="well">
            <p id="text_">
              Fruit has been recognized as a good source of vitamins and
              minerals, and for their role in preventing vitamin C and vitamin A deficiencies.
            </p>
          </div>
          <div class="well">
            <p id="text_">
              USDA's MyPlate encourages making half your plate fruits
              and vegetables for healthy eating.
            </p>
          </div>
        </div>
        <div class="col-sm-3">
          <div class="well">
            <p id="text_">
              The nutrients in fruit are vital for health and maintenance of your body.
              The potassium can reduce your risk of heart disease.
            </p>
          </div>
          <div class="well">
            <p id="text_">
              Fruit are important sources of many nutrients,
              including potassium, fiber, vitamin C and folate (folic acid).
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="container text-center"> <br><br>
      <h3>Best Fruits</h3><br>
      <br>
      <div class="row">
        <div class="col-sm-2">
          <img src="@/assets/images/6th.jpg" class="img-responsive" style="width:100%" alt="Image">
          <p>Partner 1</p>
        </div>
        <div class="col-sm-2">
          <img src="@/assets/images/7th.jpg" class="img-responsive" style="width:100%" alt="Image">
          <p>Partner 2</p>
        </div>
        <div class="col-sm-2">
          <img src="@/assets/images/8th.jpg" class="img-responsive" style="width:100%" alt="Image">
          <p>Partner 3</p>
        </div>
        <div class="col-sm-2">
          <img src="@/assets/images/9th.jpg" class="img-responsive" style="width:100%" alt="Image">
          <p>Partner 4</p>
        </div>
        <div class="col-sm-2">
          <img src="@/assets/images/10th.jpg" class="img-responsive" style="width:100%" alt="Image">
          <p>Partner 5</p>
        </div>
        <div class="col-sm-2">
          <img src="@/assets/images/11th.jpg" class="img-responsive" style="width:100%" alt="Image">
          <p>Partner 6</p>
        </div>
      </div>
    </div>
    <br>

    <footer class="container-fluid text-center" id="footer"> <br>
      <center id="footer_text">© Copyright Agency 2019.</center> <br>
    </footer>
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
      showModal: false,
      showModalLogin: false,
      newItem: "",
      errors: {},
      // emailloginverify:true,
      // passloginverify:true,
      errors1: {},
      usertype: null,
      name: null,
      email: null,
      password: null,
      items: []
    };
  },
  created() {
    if(localStorage.getItem('status')){
      next();
    }
  },
  methods: {
    register() {
      if (this.checkForm()) {
        axios
          .post(process.env.API_URL + "/register", {
            usertype: this.usertype,
            name: this.name,
            email: this.email,
            password: this.password
          })
          .then(res => {
            console.log(res);
            if (res.data.result === "email is already exists!") {
              this.$Message.error(res.data.result);
              this.usertype = "";
              this.email = "";
              this.name = "";
              this.password = "";
              this.state = "default";
            } else {
              this.$Message.success("Registered Successfully... Login Now");
              // if (res.data.result.usertype === "Retailer") {
                this.usertype = "";
                this.email = "";
                this.name = "";
                this.password = "";
                this.state = "default";
                this.showModal=false;
            }
          })
          .catch(err => {
            // console.log("error");
          });
      }
    },
    Login() {
      if (this.checkForm1()) {
        axios
          .post(process.env.API_URL + "/Login", {
            usertype: this.usertype,
            email: this.email,
            password: this.password
          })
          .then(res => {
            console.log(res)
            if (res.data.result === "Invalid Email / Password / UserType") {
              this.$Message.error(res.data.result);
              this.usertype = "";
              this.email = "";
              this.password = "";
              this.state = "default";
            } else if (res.data.result === "Invalid Password") {
              this.$Message.error(res.data.result);
              this.usertype = "";
              this.email = "";
              this.password = "";
              this.state = "default";
            } else {
              if (res.data.usertype === "Retailer") {
                let accessToken = res.data.access_token;
                localStorage.setItem('token', accessToken);
                axios.defaults.headers.common['Authorization'] = "Bearer " + accessToken;
                localStorage.setItem('user', res.data.message);
                localStorage.setItem('status', true);
                router.push({
                  name: "Sellitems",
                  params: { id: res.data.usertype }
                });
              } else {
                router.push({
                  name: "PurchaseItems",
                  params: { id: res.data.usertype }
                });
              }
            }
          })
          .catch(err => {
            console.log("Not logged in");
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            localStorage.removeItem('status');
            console.log(err);
          });
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
      if (!this.usertype) {
        this.errors.usertype = "Select your type";
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
      if (!this.usertype) {
        this.errors1.usertype = "Select your type";
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
}
a:hover {
  color: red;
}
#footer_text {
  color: white;
}
.well {
  background-color: #cccab8;
}
#text_ {
  color: #01070c;
}
#customer,
#retailer {
  height: 20px;
  width: 20px;
  color: #3490dc;
}
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

h1 {
  color: #3d4852;
}

ul {
  list-style: none;
  padding: 0;
}

a:hover {
  color: #6cb2eb;
  font-size: 1.25rem;
  transition: all 0.1s ease-in;
  margin-top: 0.5rem;
  transform: scale(1.5);
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
