<template>
  <div id="items-list">
    <router-link to="/" style="float:right;color:white;">Logout</router-link>
    <h2>Total Price:{{ totalProducts}}</h2>
    <h1>Available Fruits</h1>
    <br>
    <h4 v-for="product in products" :key="product.name">
      <table border="0">
        <tr>
          <td>
            <div id="list">
              <h4 id="productdisplay">Fruit: {{ product.name}}</h4>
              <h4 id="productdisplay">Quantity: {{ product.quantity1}}</h4>
              <h4 id="productdisplay">Rs: {{ product.price}}</h4>
              <input
                type="button"
                id="bt1"
                @click="product.quantity = (product.quantity + 1 )"
                value="+"
                class="btn btn-primary"
                :disabled="product.quantity1 <= product.quantity || product.quantity1 ===0"
              >
              <input
                type="text"
                id="qty"
                v-on:keypress="isNumber($event)"
                style="color:blue"
                value="0"
                name="quantity"
                v-model.number="product.quantity"
                :disabled="product.quantity1 <= product.quantity || product.quantity1 ===0"
              >
              <input
                type="button"
                id="bt2"
                @click="product.quantity = (product.quantity - 1 )"
                class="btn btn-primary"
                value="-"
                :disabled="product.quantity <= 0 || product.quantity1 ===0"
              >
              <br>
              <p></p>
              <span v-if="product.quantity1 === 0" style="color:red">OUT OF STOCK</span>
            </div>
          </td>
          <td id="secondDivision" v-if="product.quantity > 0">
            <h3>PRODUCTS SUMMARY</h3>
            <br>
            <h4>{{product.name}}</h4>
            <p>
              <br>
              {{product.quantity}} x Rs {{product.price}} = Rs {{product.quantity*product.price}}
            </p>
          </td>
        </tr>
      </table>
    </h4>
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
// const i = 1;
module.exports = {
  data() {
    return {
      products: [
        {
          name: 'Apple',
          quantity1: 10,
          quantity: 0,
          price: 300,
        },
        {
          name: 'Banana',
          quantity1: 0,
          quantity: 0,
          price: 400,
        },
        {
          name: 'Mango',
          quantity1: 10,
          quantity: 0,
          price: 250,
        },
        {
          name: 'Pine Apple',
          quantity1: 10,
          quantity: 0,
          price: 220,
        },
      ],
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
  methods: {
    isNumber(evt) {
      this.evt = evt || window.event;
      const charCode = evt.which ? evt.which : evt.keyCode;
      if (charCode > 31 && (charCode < 48 || charCode > 57)) { evt.preventDefault(); }
      return true;
    },
    show() {
      this.$modal.show('hello-world');
    },
  },
};
</script>
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
</style>

