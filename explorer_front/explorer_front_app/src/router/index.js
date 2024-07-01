// import Vue from 'vue';
// import VueRouter from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import DjangoDataView from '@/views/DjangoDataView.vue';
//import About from '@/views/About.vue';
import MapView from '@/views/explorerMapView.vue';
import GalapagosMapView from '@/views/GalapagosMapView.vue';
import ThreeJSView from '@/views/ThreeJSView.vue';

// Vue.use(VueRouter);

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: Home,
//   },
//   {
//     path: '/about',
//     name: 'About',
//     component: About,
//   },
//   {
//     path: '/threejs',
//     name: 'ThreeJS',
//     component: ThreeJSView,
//   },
// ];

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes,
// });

// export default router;

const routes = [
    { path: '/', name: 'HomePage', component: HomePage },
    { path: '/images', name: 'DjangoData', component: DjangoDataView },
    { path: '/map', name: 'explorerMap', component: MapView},
    { path: '/islands', name: 'GalapagosMap', component: GalapagosMapView},
    { path: '/threejs', name: 'ThreeJS', component: ThreeJSView },
  ];
  
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
  export default router;