/* eslint-disable import/no-unresolved */
/* eslint-disable no-undef */
/* eslint-disable no-unused-vars */
import Vue from 'vue';
import Router from 'vue-router';
import FirstPage from '@/components/FirstPage';
import Sellitems from '@/components/Sellitems';
import PurchaseItems from '@/components/PurchaseItems';
// import Logout from '@/components/Logout';
// import store from '../store/index';
// eslint-disable-next-line import/extensions
// import auth from '@/services/authServices.js';

Vue.use(Router);
function requireAuth(to, from, next) {
  if (localStorage.getItem('token')) {
    next(); // we are authorized, continue on to the requested route
  } else {
    next('/'); // they are not authorized, so redirect to login
  }
}

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
      beforeEnter: requireAuth,
    },
    {
      path: '/PurchaseItems',
      name: 'PurchaseItems',
      component: PurchaseItems,
      beforeEnter: requireAuth,
    },
    // {
    //   path: '/logout',
    //   name: 'Logout',
    //   component: Logout
    // },
  ],
  mode: 'history',
});
// const openRoutes = ['Login', 'Signup'];

// // eslint-disable-next-line no-undef
// router.beforeEach((to, from, next) => {
//   if (localStorage.getItem('user')) {
//     next();
//   } else {
//     next('false');
//   }
// });
