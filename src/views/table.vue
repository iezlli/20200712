<template>
    <div class="about">
        <el-table :data="tableData" style="width: 100%">
            <el-table-column label="姓名" prop="name">
            </el-table-column>
            <el-table-column label="性别" prop="sex">
            </el-table-column>
            <el-table-column align="right">
                <template slot="header" slot-scope="scope">
                    <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">隐藏</el-checkbox>
                </template>
                <template slot-scope="scope">
                    <el-checkbox v-model="scope.row.checked" @change="handleCheckOneChange">隐藏</el-checkbox>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tableData: [
                {
                    name: "李时珍",
                    sex: "男",
                    checked: false
                },
                {
                    name: "花木兰",
                    sex: "女",
                    checked: true
                }
            ],
            checkAll: false,
            isIndeterminate: false
        };
    },
    methods: {
        handleCheckAllChange(val) {
            console.info("check all change is ", val);
            this.isIndeterminate = false;
            this.tableData.forEach(item => {
                item.checked = val;
            });
        },
        handleCheckOneChange(val) {
            console.info("check one change is ", val);
            let totalCount = this.tableData.length;
            let someStatusCount = 0;
            this.tableData.forEach(item => {
                if (item.checked === val) {
                    someStatusCount++;
                }
            });
            this.checkAll = totalCount === someStatusCount ? val : !val;
            this.isIndeterminate =
                someStatusCount > 0 && someStatusCount < totalCount;
        }
    }
};
</script>

<style lang="scss" scoped>
$color: red;
.about {
    border: 1px solid $color;
    &::before {
        content: "";
    }
}
</style>