/* eslint-disable */
import '@vue/test-utils'
module.exports = {
    post: jest.fn(() => Promise.resolve({ data: [3] }))
}