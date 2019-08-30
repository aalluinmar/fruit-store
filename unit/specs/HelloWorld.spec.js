import Vue from 'vue';
import FirstPage from '@/components/FirstPage';

describe('HelloWorld.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(FirstPage);
    const vm = new Constructor().$mount();
    expect(vm.$el.querySelector('.hello h1').textContent);
  });
});
