<template>

    <footer>
        <router-link :to="{ name: 'HomePage' }" class="footerLinks">
                Home
        </router-link>
        <router-link :to="{ name: 'FAQPage' }" class="footerLinks">
                FAQs
        </router-link>
        <router-link :to="{ name: 'PingTest' }" class="footerLinks">
                Index Constituents
        </router-link>
        <router-link :to="{ name: 'TimeSeries' }" class="footerLinks">
                Time Series
        </router-link>
        <router-link :to="{ name: 'StatsPage' }" class="footerLinks">
                Statistics
        </router-link>
        <p class="footerText">Copyright © 2022 Faculty of Commerce - University of Cape Town</p>
    </footer>

</template>

<style>
    footer {
	background-color: #1D70B7;
	padding: 0.1%;
	padding-top: 0.9%;
    }

    .footerLinks {
	padding: 5%;
	padding-bottom: 3%;
	padding-top: 2%;
    }

    .footerText {
	margin-top: 0.5%;
	color: white;
	font-size: medium;
	text-align: center;
    }

</style>