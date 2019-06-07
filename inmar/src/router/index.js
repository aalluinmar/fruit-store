import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Sellitems from '@/components/Sellitems';
import PurchaseItems from '@/components/PurchaseItems';

Vue.use(Router);

function requireAuth(to, from, next) {
  if (localStorage.getItem('token')) {
  next(); // we are authorized, continue on to the requested route
  } else {
  next('/'); // they are not authorized, so redirect to login
  }
  }
  

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
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
  ],
});
