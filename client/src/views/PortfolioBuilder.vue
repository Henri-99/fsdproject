<template>
    <div>
        
        <div class="flex-container">
            <div style="flex-grow: 1">
                <table class="pfTable">
                    <th>#</th>
                    <th>Stock</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Total</th>
                    <th>Weight</th>
                    <tr><button @click="add">+</button></tr>
                    <tr v-for="stock in n" :key="stock">
                            <td>{{ stock }}</td>
                            <td><input v-model=name[stock-1] style="width:80px"></td>
                            <td><input v-model=quantity[stock-1] style="width:60px"></td>
                            <td>{{ price[stock-1] }}</td>
                            <td>{{ total[stock-1] }}</td>
                            <td>{{ weight[stock-1]}}</td>
                            <td><button @click="remove(stock-1)">x</button></td>
                    </tr>
                    
                </table>

                    
                <button @click="retrieve" style="margin:10px 2px 10px 2px">Analyze</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'PortfolioBuilder',
	data() {
		return {
			n: 1,
            name: [],
            quantity : [],
            price : [],
            total : [],
            weight : [],
            stockdata : [],
		};
	},
	methods: {
        add() {
            this.n = this.n + 1;
            this.name.push('');
            this.quantity.push('');
            this.price.push('');
            this.total.push('')
            this.weight.push('');
        },
        remove(i) {
            if (this.n > 0) {
                this.n = this.n - 1;
                this.name.splice(i, 1);
                this.quantity.splice(i, 1);
                this.price.splice(i, 1);
                this.total.splice(i, 1);
                this.weight.splice(i, 1);
            }
        },
        update(res){
            console.log(res);
        },
        retrieve() {
            axios.post('http://localhost:5000/pf',
                {
                    stocks: this.name,
                    quantities: this.quantity
                })
                .then((response) => {
                    this.stockdata = response.data;
                    for (let i = 0; i < this.stockdata.length; i++) {
                        this.price[i] = this.stockdata[i].price;
                        this.total[i] = this.stockdata[i].total;
                        this.weight[i] = this.stockdata[i].weight;
                    }
                    
                })

        },
    }
}
</script>

<style>
.pfTable {
	margin-left: auto;
	margin-right: auto;
	border-collapse: collapse;
	padding: 0 20rem 0 0;
}

.pfTable td {
  padding: 0 0.3rem 0 0.3rem;
}

.pfTable tr:nth-child(odd) {
	background-color: #fdfcfc;
}
.pfTable tr:nth-child(even) {
	background-color: #f2f2f2;
}

.pfTable tr:hover {
	background-color: #ddd;
}

.pfTable th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align:center;
	background-color: #348bd6;
	color: white;
	width: 6rem;
}</style>