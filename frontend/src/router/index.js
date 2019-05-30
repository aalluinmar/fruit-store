import Vue from 'vue';
import Router from 'vue-router';
import FirstPage from '@/components/FirstPage';
import Sellitems from '@/components/Sellitems';
import PurchaseItems from '@/components/PurchaseItems';
// import auth from '@/services/authService';

Vue.use(Router);
// function requireAuth(to, from, next) {
//   if (auth.getAuthStatus) {
//     next(); // we are authorized, continue on to the requested route
//   } else {
//     next('/'); // they are not authorized, so redirect to login
//   }
// }

export default new Router({
  routes: [
    {
      path: '/',
      name: 'FirstPage',
      component: FirstPage,
    },
    {
      path: '/Sellitems',
      name: 'Sellitems',
      component: Sellitems,
    },
    {
      path: '/PurchaseItems',
      name: 'PurchaseItems',
      component: PurchaseItems,
    },
  ],
  mode: 'history',
});
