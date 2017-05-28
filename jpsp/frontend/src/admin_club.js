// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminClub from './AdminClub.vue'
import router from './router/admin_club.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import Vuex from 'vuex'
Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(Vuex)
/* eslint-disable no-new */
const AdminClubVuexStore = new Vuex.Store({
  state: {
    ClubId: '',
    CludName: '',
    Token: ''
  },
  mutations: {
    login (state) {
      alert(state.user_name)
    }
  }
})

new Vue({
  el: '#app_club',
  router,
  store: AdminClubVuexStore,
  template: '<App/>',
  components: {AdminClub},
  render: h => h(AdminClub)
})
