/* eslint-disable no-unused-vars */
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import iView from 'iview/dist/iview';
import axios from 'axios';
import 'iview/dist/styles/iview.css';
import locale from 'iview/dist/locale/en-US';
import BootstrapVue from 'bootstrap-vue';
import VModal from 'vue-js-modal';
import Vue from 'vue';
import App from './App';
import router from './router';

window.axios = axios;
window.token = localStorage.getItem('token');
window.user = localStorage.getItem('user');
// eslint-disable-next-line no-template-curly-in-string
axios.defaults.headers.common.Authorization = 'Bearer ${  window.token}';
axios.defaults.headers.post['Content-Type'] = 'application/json';
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
