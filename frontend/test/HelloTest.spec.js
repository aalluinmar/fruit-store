/* eslint-disable */
// jest.mock('axios', () => ({
//   post: jest.fn()
// }))
import axios from 'axios'
import 'jest-localstorage-mock'
import { createLocalVue, shallowMount } from '@vue/test-utils'
import VueRouter from 'vue-router'
import iView from 'iview/dist/iview'
import FirstPage from '../src/components/FirstPage'

describe('FirstPage.vue', () => {
  // process.env.API_URL="http://localhost:8000"
  const localVue = createLocalVue()
  localVue.use(VueRouter)
  localVue.use(iView)

  beforeEach(() => {
    // console.log("---------------------beforeEach-------------------------------")
  });

  afterEach(() => {
    // console.log("---------------------afterEach-------------------------------")
    localStorage.removeItem('KEY')
  });
  
  it('navbar items', () => {
    const wrapper = shallowMount(FirstPage)
    expect(wrapper.find('nav').is('nav')).toBe(true);
    expect(wrapper.find('p').name()).toBe('p');
    expect(wrapper.find('p.navbar-brand').text()).toBe('FRUIT STORE');
    expect(wrapper.find('a').name()).toBe('a');
    expect(wrapper.find('a.home').text()).toBe('Home');
    expect(wrapper.find('a.about').text()).toBe('About');
    expect(wrapper.find('a.info').text()).toBe('Contact');

  })
  it('Calls axios.post in Registration', () => {
      const wrapper = shallowMount(FirstPage, {
        mocks: {
          axios
        }
      })
      //checking script tag items
      expect(wrapper.is(FirstPage)).toBe(true);
      expect(wrapper.vm.items.length).toBe(0)
      expect(wrapper.vm.showModal).toBe(false)

      //triggering the show-modal for Registration
      expect(wrapper.find('a#show-modal').name()).toBe('a');
      expect(wrapper.find('a#show-modal').text()).toMatch('SignUp');
      wrapper.find('a#show-modal').trigger('click')
      expect(wrapper.find('h4.modal-title').text()).toMatch('Registration')
      expect(wrapper.vm.showModal).toBe(true)
      //Checking the Tag names
      expect(wrapper.find('#usertype').name()).toBe('RadioGroup')
      expect(wrapper.find('#retailer_radio').name()).toMatch('Radio')
      expect(wrapper.find('#customer_radio').name()).toMatch('Radio')
      expect(wrapper.find('#RegisterName').name()).toBe('Input')
      expect(wrapper.find('#RegisterEmail').name()).toBe('Input')
      expect(wrapper.find('#RegisterPass').name()).toBe('Input')
      expect(wrapper.find('#registerSubmit').name()).toBe('button')

      //Finding the tags with their Id's
      const user_type = wrapper.find('#usertype')
      const name = wrapper.find('#RegisterName')
      const email = wrapper.find('#RegisterEmail')
      const pass = wrapper.find('#RegisterPass')

      //Checking the values to be empty for tags
      expect(name.text()).toMatch('')
      expect(email.text()).toMatch('')
      expect(pass.text()).toMatch('')
      expect(user_type.text()).toMatch('')
      expect(wrapper.find('#retailer_radio').text()).toMatch('Retailer')
      expect(wrapper.find('#customer_radio').text()).toMatch('Customer')
      expect(wrapper.find('#registerSubmit').text()).toMatch('Register')

      //Setting Data to the vue models
      wrapper.setData({
        usertype: 'Retailer',
        name: 'Test',
        email: 'test@gmail.com',
        password: 'Test@123'
      })

      //Assigning the values to attributes
      expect(name.attributes().value).toMatch('Test')
      expect(email.attributes().value).toMatch('test@gmail.com')
      expect(pass.attributes().value).toMatch('Test@123')
      expect(user_type.attributes().value).toMatch('Retailer')

      //Checking the errors for the form validation
      expect(wrapper.find('#alert').exists()).toBe(true)
      expect(wrapper.find('#alert1').exists()).toBe(true)
      expect(wrapper.find('#alert2').exists()).toBe(true)  
      expect(wrapper.find('#alert3').exists()).toBe(true)

      //Triggering the submit button after the details assigned
      wrapper.find('#registerSubmit').trigger('submit')
      const url = process.env.API_URL + "/register"

      wrapper.checkForm
      
      expect(axios.post).toHaveBeenCalledWith(url, {
        usertype: 'Retailer',
        name: 'Test',
        email: 'test@gmail.com',
        password: 'Test@123'
      })
      //Setting localStorage
      const value = email.attributes().value
      localStorage.setItem('KEY',value)
      console.log(localStorage.getItem('KEY'))
  })
  it('Calls axios.post in Login', () => {
    const wrapper = shallowMount(FirstPage, {
      mocks: {
        axios
      }
    })
    console.log(localStorage.getItem('KEY'))
    //triggering the show-modal for Registration
    expect(wrapper.find('a#show-modal-Login').name()).toBe('a');
    expect(wrapper.find('a#show-modal-Login').text()).toMatch('Login');
    wrapper.find('a#show-modal-Login').trigger('click')
    expect(wrapper.find('h4.modal-title').text()).toMatch('Login')

    //Checking the Tag names
    expect(wrapper.find('#usertypeLogin').name()).toBe('RadioGroup')
    expect(wrapper.find('#retailer_radio_login').name()).toMatch('Radio')
    expect(wrapper.find('#customer_radio_login').name()).toMatch('Radio')
    expect(wrapper.find('#emailLogin').name()).toBe('Input')
    expect(wrapper.find('#passLogin').name()).toBe('Input')
    expect(wrapper.find('#loginSubmit').name()).toBe('button')

    //Finding the tags with their Id's
    const user_type = wrapper.find('#usertypeLogin')
    const email = wrapper.find('#emailLogin')
    const pass = wrapper.find('#passLogin')

    //Checking the values to be empty for tags
    expect(user_type.text()).toMatch('')
    expect(email.text()).toMatch('')
    expect(pass.text()).toMatch('')
    expect(wrapper.find('#retailer_radio_login').text()).toMatch('Retailer')
    expect(wrapper.find('#customer_radio_login').text()).toMatch('Customer')
    expect(wrapper.find('#loginSubmit').text()).toMatch('Login')

    //Setting Data to the vue models
    wrapper.setData({
      usertype: 'Retailer',
      email: 'test123@gmail.com',
      password: 'Test@123'
    })

    //Assigning the values to attributes
    expect(user_type.attributes().value).toMatch('Retailer')
    expect(email.attributes().value).toMatch('test123@gmail.com')
    expect(pass.attributes().value).toMatch('Test@123')

    //Checking the errors for the form validation
    expect(wrapper.find('#alert4').exists()).toBe(true)
    expect(wrapper.find('#alert5').exists()).toBe(true)
    expect(wrapper.find('#alert6').exists()).toBe(true)  

    //Triggering the submit button after the details assigned
    wrapper.find('#loginSubmit').trigger('submit')
    const url = process.env.API_URL + "/Login"
    wrapper.created
    wrapper.checkForm1
    wrapper.validEmail
    wrapper.validPassword
    expect(axios.post).toHaveBeenCalledWith(url, {
      usertype: 'Retailer',
      email: 'test123@gmail.com',
      password: 'Test@123'
    })
    //Setting localStorage
    const value = email.attributes().value
    localStorage.setItem('KEY',value)
    console.log(localStorage.getItem('KEY'))

    
  })
  it('Carousel images text checking', () => {
    const wrapper = shallowMount(FirstPage)

    //checking tags names
    expect(wrapper.find('#carousel_text-1').name()).toBe('h3');
    expect(wrapper.find('#carousel_text-2').name()).toBe('h3');
    expect(wrapper.find('#carousel_text-3').name()).toBe('h3');
    expect(wrapper.find('#carousel_text-4').name()).toBe('h3');
    expect(wrapper.find('#carousel_text-5').name()).toBe('h3');

    //Counting div tags
    expect(wrapper.findAll('div').length).toBe(40)
    //Checking tags text
    expect(wrapper.find('#carousel_text-1').text()).toMatch('A Healthy outside starts from the inside')
    expect(wrapper.find('#carousel_text-2').text()).toMatch('You are What you eat')
    expect(wrapper.find('#carousel_text-3').text()).toMatch('Food is Fuel not Therapy')
    expect(wrapper.find('#carousel_text-4').text()).toMatch('Don\'t eat less eat right')
    expect(wrapper.find('#carousel_text-5').text()).toMatch('Healthy Food Healthy Life')

    //checking container text-center text

    expect(wrapper.find('#Use_Of_Fruits').text()).toMatch('Use Of Fruits');
    expect(wrapper.find('#Best_Protien_Fruit').text()).toMatch('Best Protien Fruit');
    expect(wrapper.find('#Protect_against_Cancer').text()).toMatch('Protect against Cancer');
    expect(wrapper.find('#Best_Fruits').text()).toMatch('Best Fruits');
    
    expect(wrapper.find('#Partner_1').text()).toMatch('Partner 1');
    expect(wrapper.find('#Partner_2').text()).toMatch('Partner 2');
    expect(wrapper.find('#Partner_3').text()).toMatch('Partner 3');
    expect(wrapper.find('#Partner_4').text()).toMatch('Partner 4');
    expect(wrapper.find('#Partner_5').text()).toMatch('Partner 5');
    expect(wrapper.find('#Partner_6').text()).toMatch('Partner 6');

    expect(wrapper.find('#footer_text').text()).toMatch('© Copyright Agency 2019.');

    expect(wrapper.find('#text_1').text()).toMatch('Fruit has been recognized as a good source of vitamins and minerals, and for their role in preventing vitamin C and vitamin A deficiencies.')
    expect(wrapper.find('#text_2').text()).toMatch('USDA\'s MyPlate encourages making half your plate fruits and vegetables for healthy eating.')
    expect(wrapper.find('#text_3').text()).toMatch('The nutrients in fruit are vital for health and maintenance of your body. The potassium can reduce your risk of heart disease.')
    expect(wrapper.find('#text_4').text()).toMatch('Fruit are important sources of many nutrients, including potassium, fiber, vitamin C and folate (folic acid).')
  })
})
