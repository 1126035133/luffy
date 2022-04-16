import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'


// 导入axios
import axios from 'axios';  // 导入安装的axios
Vue.prototype.$axios = axios;  // 相当于把axios这个对象放到了Vue对象中， 以后用：vue.对象.$axios

// 导入cookies操作
import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies;

// 导入element-ui页面组件框架
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// import 'jquery'
// import 'jquery/dist/jquery.min.js'

// 导入bootstrap
// import $ from 'jquery'
// import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.min.css'

// import $ from 'jquery'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap/dist/js/bootstrap.min.js'




// 配置全局样式
import '@/assets/css/global.css'

// 配置全局自定义设置
import settings from '@/assets/js/settings'
Vue.prototype.$settings = settings;
// 在所有需要与后台交互的组件中：this.$settings.base_url + '再拼接具体后台路由'


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
