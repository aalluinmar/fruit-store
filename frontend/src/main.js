// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import locale from 'iview/dist/locale/en-US';
import BootstrapVue from 'bootstrap-vue';
import VModal from 'vue-js-modal';
import Vue from 'vue';
import App from './App';
import router from './router';


// import axios from 'axios';

Vue.use(BootstrapVue);
Vue.config.productionTip = false;
Vue.use(VModal);

Vue.use(iView, { locale });
// Vue.use(VueAxios, axios);
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
