import { shallowMount } from '@vue/test-utils';
import FirstPage from 'FirstPage';



describe('FirstPage', () => {
    it('increments or decrement count when button is clicked', () => {
        const wrapper = shallowMount(FirstPage)
        const message = wrapper.find('p.navbar-brand').text();
        // const message1 = wrapper.find('h3').text();
        expect(message).toBe('FRUIT STORE');
        // expect(message1).toBe('aravind');
    })
})