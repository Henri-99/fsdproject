<template>
	<div class="flex-container statform">
		<div>
			<select v-model="quarter">
				<option disabled value="">Select Date</option>
				<option v-for="quarter in dates" :key="quarter">{{ quarter }}</option>
			</select>
		</div>
		<div>
			<select v-model="indexCode">
				<option disabled value="">Select Index</option>
				<option v-for="index in indices" :key="index">{{ index }}</option>
			</select>
		</div>
	</div>

	<div class="flex-container" v-if="indexCode">
		<div>
			<table class="stocklist" v-if="indexCode">
				<tr>
					<th>Stock</th>
					<th>Weight</th>
				</tr>
				<tr v-for="stock in msg" :key="stock">
					<td>{{ stock.name }} </td>
					<td>{{ (stock.value * 100).toFixed(2) }} % </td>
				</tr>
			</table>
		</div>


		<div>
			<PieChart :key="quarter" :indexName="indexCode" :data="msg" />
			<p style='font-size : 0.7rem; color : lightgray'>SMALL consists of all stocks having<br /> a weight less
				than 0.5% </p>
		</div>

	</div>
</template>

<script>
import axios from 'axios';
import PieChart from '../components/charts.vue';

export default {
	name: 'PingTest',
	components: {
		PieChart,
	},
	data() {
		return {
			msg: '',
			indexCode: '',
			res: {},
			quarter: '',
		};
	},
	methods: {
		getMessage() {
			const path = 'http://localhost:5000/ping?index='.concat(this.indexCode, '&q=', this.quarter);
			axios.get(path)
				.then((res) => {
					this.msg = res.data;
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},
	},
	watch: {
		indexCode() {
			if (this.quarter !== '') {
				this.getMessage();
			}
		},
		quarter() {
			if (this.indexCode !== '') {
				this.getMessage();
			}
		},
	},
	created() {
		this.indices = ["ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY", "ALTI"];
		this.dates = ['2021Q1','2020Q4','2020Q3','2020Q2','2020Q1','2019Q4','2019Q3','2019Q2','2019Q1','2018Q4','2018Q3','2018Q2','2018Q1','2017Q4','2017Q3'];
	},

};
</script>

<style>
.stocklist {
	margin-left: auto;
	margin-right: 0;
	border-collapse: collapse;
}

.stocklist td,
.stocklist th {
	border: 1px solid #ddd;
	padding: 3px 10px 3px 10px;
}

.stocklist tr:nth-child(even) {
	background-color: #f2f2f2;
}

.stocklist tr:hover {
	background-color: #ddd;
}

.stocklist th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align:center;
	background-color: #348bd6;
	color: white;
	width: 6rem;
}

.flex-container {
    display: flex;
	justify-content: center;
}

</style>