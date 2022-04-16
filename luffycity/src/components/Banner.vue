<template>
    <el-carousel height="450px" :interval="3000" arrow="always">
        <el-carousel-item v-for="item in banner_list">
            <router-link :to="item.link">
                <img :src="item.img" :alt="item.name">
            </router-link>
        </el-carousel-item>
<!--        <el-carousel-item>-->
<!--            <img src="@/assets/img/banner2.png" alt="">-->
<!--        </el-carousel-item>-->
<!--        <el-carousel-item>-->
<!--            <img src="@/assets/img/banner3.png" alt="">-->
<!--        </el-carousel-item>-->
    </el-carousel>
</template>



<script>
    export default {
        name: "Banner",

        data(){
            return {
                banner_list:[]
            }
        },
        created(){
            this.GetBannerList();

        },

        methods:{
            GetBannerList(){
                this.$axios({
                    headers: {
                        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywidXNlcm5hbWUiOiJhaDc4IiwiZXhwIjoxNjUwMzQ2MzQxLCJlbWFpbCI6IjJAcXEuY29tIn0.pbdjf4DcTUuH0QhZa5xOyje_9iIN7Pg0wuunfKwPyf8'
                    },
                    method: 'get',
                    url: this.$settings.base_url + '/home/banner/',

                    }).then(response=>{
                        this.banner_list=response.data
                    }).catch(error=>{
                        console.log(error)
                    })
            }
        }
    }

</script>

<style scoped>
    .el-carousel__item h3 {
        color: #475669;
        font-size: 10px;
        opacity: 0.75;
        line-height: 300px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
    .el-carousel__item img {
        text-align: center;
        height: 450px;

        margin: 0 auto;
        margin-left: calc(40% - 1920px / 2);
        display: block;
    }
</style>
