import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
<<<<<<< HEAD
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
=======
import './assets/tailwind.css'
>>>>>>> 7134a108d00d79e9cdff2b8b397ca5054eec34eb

createApp(App).use(router).mount('#app')
