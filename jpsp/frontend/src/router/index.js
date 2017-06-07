import Vue from 'vue'
import Router from 'vue-router'
// import index from '@/pages/index/index'
Vue.use(Router)

import index from '../pages/index/index.vue'
import Login from '../pages/index/Login.vue'
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: index
    },
    {
      path: '/test',
      name: 'test',
      component: Login
    }
  ]
})