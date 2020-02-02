import Vue from 'vue'
import App from './App'
import VueNativeSock from 'vue-native-websocket'

Vue.use(VueNativeSock, 'ws://127.0.0.1:8000/ws/', {format: "json"})
Vue.config.productionTips = false

new Vue({
    render: h => h(App)
}).$mount('#app')