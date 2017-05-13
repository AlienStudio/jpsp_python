// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminClub from './AdminClub.vue'
import router from './router/admin_club.js'
import ElementUI from 'element-ui'
Vue.config.productionTip = false

Vue.use(ElementUI)

/* eslint-disable no-new */

new Vue({
  el: '#app_club',
  router,
  template: '<App/>',
  components: { AdminClub },
  render: h => h(AdminClub)
})
