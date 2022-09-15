<template>
	<div class="flex-container statform">
		<div>
			<input  v-model="stock" placeholder="Enter stock ticker">
			<input  v-model="stock2" placeholder="Enter stock ticker">
				<!-- <option disabled value="">Select Stock</option>
				<option v-for="stock in stocks" :key="stock">{{ stock }}</option> -->
		</div>
	</div>
	<LineChart :data="msg" />
</template>

<script>
import axios from 'axios';
import LineChart from '../components/linechart.vue';


export default {
	name: 'TimeSeries',
	components: {
		LineChart
	},
	data() {
		return {
			msg: '',
			stock: '',
		};
	},
	methods: {
		getMessage() {
			const path = 'http://localhost:5000/stock?&s='.concat(this.stock);
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
	created() {
		this.stocks = ['NPN','MTN',];
	
	},
	watch: {
		stock() {
			if (this.stock.length > 2){
				this.getMessage();
			}
		}
	}
};
</script>

<style>
.center {
	margin-left: auto;
	margin-right: auto;
	border-collapse: collapse;
}

.center td,
.center th {
	border: 1px solid #ddd;
	padding: 3px 10px 3px 10px;
}

.center tr:nth-child(even) {
	background-color: #f2f2f2;
}

.center tr:hover {
	background-color: #ddd;
}

.center th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #348bd6;
	color: white;
}

.flex-container {
    display: flex;
}
.flex-child {
    flex: 1;
}  
</style>