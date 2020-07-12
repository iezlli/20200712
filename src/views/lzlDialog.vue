<template>
    <div>
        <el-dialog title="12" :visible="visible" :before-close="back" @open="open">
            <el-table :data="tabledata">
                <el-table-column width="35">
                    <template slot="header">
                        <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange"></el-checkbox>
                    </template>
                    <template slot-scope="scope">
                        <el-checkbox v-model="scope.row.checked" @change="handleCheckOneChange($event,scope.row)"></el-checkbox>
                    </template>
                </el-table-column>
                <el-table-column label="id" prop="id"></el-table-column>
                <el-table-column label="name" prop="name"></el-table-column>
            </el-table>

            <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="current" :page-sizes="[3, 200, 300, 400]" :page-size=size layout="sizes, prev, pager, next" :total="total">
            </el-pagination>

            <div slot="footer">
                <el-button @click="back">返回</el-button>
                <el-button @click="confirm">确定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
export default {
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        dataorg: {
            type: Array,
            default() {
                return [];
            }
        }
    },
    // computed: {
    //    checkAll() {
    //     return this.tabledata.every(item => item.checked)
    //    } ,
    //    isIndeterminate() {
    //        if(this.checkAll) {
    //            return false
    //        }
    //         return this.tabledata.some(item => item.checked)
    //    }
    // },
    data() {
        return {
            size: 3,
            current: 1,
            total: 0,
            tabledata: [],
            checkAll: false,
            isIndeterminate: false,
            data:[]
        };
    },

    methods: {
        handleCheckAllChange(val) {
            console.info("check all change is ", val);
            this.isIndeterminate = false;
            this.tabledata.forEach(item => {
                item.checked = val;
                if(val) {
                    this.data.push(item.id)
                    this.data=Array.from(new Set(this.data))
                }else {
                    this.data.splice(this.data.indexOf(item.id),1)
                }
            });
            
        },
        handleCheckOneChange(val,b,c) {
            // console.log(a,b,c);
            if(val){
                if(this.data.indexOf(b.id) == -1) {
                    this.data.push(b.id)
                }
            
            }else{
                this.data.splice(this.data.indexOf(b.id),1)
            }
            
            console.info("check one change is ", val);
            let totalCount = this.tabledata.length;
            let someStatusCount = 0;
            this.tabledata.forEach(item => {
                if (item.checked === val) {
                    someStatusCount++;
                }
            });
            this.checkAll = totalCount === someStatusCount ? val : !val;
            this.isIndeterminate =
                someStatusCount > 0 && someStatusCount < totalCount;
        },
        open() {
            console.log("op");
            this.data=Array.from(this.dataorg)
            this.current = 1;
            this.total = 9;
            this.tabledata = [
                {
                    id: "1",
                    name: "1"
                },
                {
                    id: "2",
                    name: "2"
                },
                {
                    id: "3",
                    name: "3"
                }
            ];
            console.log("getdata:" + this.data);
            var count = 0;
            this.tabledata.forEach(item => {
                if (this.data.indexOf(item.id) > -1) {
                    count++;
                    item.checked = true;
                } else {
                    item.checked = false;
                }
            });
            console.log(count);
            if (count == 0) {
                this.isIndeterminate = false;
                this.checkAll = false;
            } else if (count > 0 && count < this.tabledata.length) {
                this.isIndeterminate = true;
                this.checkAll = false;
            } else {
                this.isIndeterminate = false;
                this.checkAll = true;
            }
        },
        back() {
            this.$emit("handleCancel");
        },
        confirm() {
            this.$emit("handleconfirm", this.data);
        },
        handleSizeChange() {},
        handleCurrentChange(current) {
            this.total = 9;
            this.current = current;
            if (current == 1) {
                this.tabledata = [
                    {
                        id: "1",
                        name: "1"
                    },
                    {
                        id: "2",
                        name: "2"
                    },
                    {
                        id: "3",
                        name: "3"
                    }
                ];
            } else if (current == 2) {
                this.tabledata = [
                    {
                        id: "4",
                        name: "4"
                    },
                    {
                        id: "1",
                        name: "1"
                    },
                    {
                        id: "6",
                        name: "6"
                    }
                ];
            } else {
                this.tabledata = [
                    {
                        id: "7",
                        name: "7"
                    },
                    {
                        id: "2",
                        name: "2"
                    },
                    {
                        id: "9",
                        name: "9"
                    }
                ];
            }
        }
    }
};
</script>

<style lang="scss" scoped>
</style>