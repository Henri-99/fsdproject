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
		<div>
			<select v-model="mktIndex">
				<option disabled value="">Select Market Proxy</option>
				<option v-for="mktI in mktIndices" :key="mktI">{{ mktI }}</option>
			</select>
		</div>
	</div>

	<div class="flex-container">
		The portfolio beta is: {{ pfBeta }}
		<br />The portfolio Systematic Variance is: {{ pfSysVol }}
		<br />The portfolio Specific Variance is: {{ pfSpecVol }}
		<br />The portfolio Variance is: {{ pfVol }}

	</div>
	<div class="flex-container statform">
		<div>
			<select v-model="stat">
				<option disabled value="">Select Statistic</option>
				<option v-for="stat in stats" :key="stat">{{ stat }}</option>
			</select>
		</div>
	</div>

	<div class="flex-container">
		<div style="flex-grow: 1">
			<table class="statmatrix" v-if="indexCode">
				<tr v-for="stock in msg" :key="stock">
					<!-- <td v-for="col in stock" :key="col"> {{ col.toFixed(5) }} </td> -->
					<div v-if="stock.constructor === Array">
						<td>{{ stock }}</td>
						<!-- <td v-for="col in stock" :key="col">{{col}}</td> -->
					</div>
					<div v-else>
						<td>{{ stock }}</td>
					</div>
				</tr>
			</table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'StatsPage',
	data() {
		return {
			msg: '',
			indexCode: '',
			mktIndex : '',
			stat : '',
			res: {},
			quarter: '',
			pfBeta: 0,
			pfSysVol: 0,
			pfSpecVol: 0,
			pfVol: 0,
		};
	},
	methods: {
		getPortfolio(){
			const path = 'http://localhost:5000/pfstats?index='.concat(this.indexCode, '&market=', this.mktIndex, '&q=', this.quarter);
			axios.get(path)
			.then((res) => {
				this.pfBeta = res.data.pfBeta
				this.pfSysVol = res.data.pfSysVol
				this.pfSpecVol = res.data.pfSpecVol
				this.pfVol = res.data.pfVol
			});

		},
		getMessage() {
			const path = 'http://localhost:5000/stat?index='.concat(this.indexCode, '&market=', this.mktIndex, '&s=', this.stat, '&q=', this.quarter);
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
			if (this.mktIndex !== ''  && this.quarter !== '') {
				this.getPortfolio();
			}
			if (this.mktIndex !== '' && this.stat !== '' && this.quarter !== '') {
				this.getMessage();
			}
		},
		mktIndex() {
			if (this.indexCode !== ''  && this.quarter !=='') {
				this.getPortfolio();
			}
			if (this.indexCode !== '' && this.stat !== '' && this.quarter !=='') {
				this.getMessage();
			}
		},
		stat() {
			if (this.mktIndex !== '' && this.indexCode !== '' && this.quarter !=='') {
				this.getMessage();
			}
			// if (this.stat == )
		},
		quarter() {
			if (this.mktIndex !== '' && this.indexCode !== '') {
				this.getPortfolio();
			}
			if (this.mktIndex !== '' && this.indexCode !== '' && this.stat !=='') {
				this.getMessage();
			}
		},
	},
	created() {
		this.indices = ["ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY", "ALTI"];
		this.mktIndices = ["J200", "J203", "J250", "J257", "J258"];
		this.stats = ['beta', 'specVols', 'sysCov', 'specCov', 'totCov', 'corrMat'];
		this.dates = ['2021Q1','2020Q4','2020Q3','2020Q2','2020Q1','2019Q4','2019Q3','2019Q2','2019Q1','2018Q4','2018Q3','2018Q2','2018Q1','2017Q4','2017Q3'];
	},

};
</script>

<style>

.flex-container {
    display: flex;
}

.statform {
	justify-content: center;
	padding-bottom: 1rem;
}

select {
	padding: 0.5rem 0.5rem 0.5rem 0.5rem ;
	background-color: #f0fdfa;
	border-radius: 15px;
	margin-left: 0.5rem;
	margin-right: 0.5rem;
	/* text-align: center; */
}

.statmatrix {
	margin-left: auto;
	margin-right: auto;
	border-collapse: collapse;
	padding: 0 20rem 0 0;
}

.statmatrix td {
  padding: 0 0.3rem 0 0.3rem;
}

.statmatrix tr:nth-child(odd) {
	background-color: #fdfcfc;
}
.statmatrix tr:nth-child(even) {
	background-color: #f2f2f2;
}

.statmatrix tr:hover {
	background-color: #ddd;
}

.statmatrix th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align:center;
	background-color: #348bd6;
	color: white;
	width: 6rem;
}

</style>