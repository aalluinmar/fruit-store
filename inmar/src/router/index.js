import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Sellitems from '@/components/Sellitems';
import PurchaseItems from '@/components/PurchaseItems';

Vue.use(Router);

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
    },
    {
      path: '/PurchaseItems',
      name: 'PurchaseItems',
      component: PurchaseItems,
    },
  ],
});
