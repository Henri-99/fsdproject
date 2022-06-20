import about from "./components/about.vue"
import Shares from "./components/Shares.vue"
import charts from "./components/charts.vue"
import Home from "./components/Home.vue"
import Indicies from "./components/Indicies.vue"
import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
    {
        name: "about",
        component: about,
        path: "/about",
    },
    {
        name: "Shares",
        component: Shares,
        path: "/Shares",
    },
    {
        name: "charts",
        component: charts,
        path: "/charts",
    },
    {
        name: "Home",
        component: Home,
        path: "/Home",
    },
    {
        name: "Indicies",
        component: Indicies,
        path: "/Indicies",
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});