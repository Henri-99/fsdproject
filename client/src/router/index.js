import { createWebHistory, createRouter } from 'vue-router'
import HomePage from "@/views/HomePage.vue"
import FAQPage from "@/views/FAQPage.vue"
import TimeSeries from "@/views/TimeSeries.vue"
import PingTest from '@/views/Ping.vue'
import StatsPage from '@/views/StatsPage.vue'
import PageNotFound from "@/views/PageNotFound.vue"
import PortfolioBuilder from "@/views/PortfolioBuilder.vue"

const routes = [{
        path: '/',
        name: 'HomePage',
        component: HomePage,
    }, {
        path: '/faq',
        name: 'FAQPage',
        component: FAQPage,
    }, {
        path: '/ping',
        name: 'PingTest',
        component: PingTest,
    }, {
        path: '/time',
        name: 'TimeSeries',
        component: TimeSeries,
    },
    {
        path: '/stats',
        name: 'StatsPage',
        component: StatsPage,
    },
    {
        path: '/myPortfolio',
        name: 'PortfolioBuilder',
        component: PortfolioBuilder
    },
    {
        path: '/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router