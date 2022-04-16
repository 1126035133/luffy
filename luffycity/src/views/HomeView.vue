<template>
  <div class="home">
        <Header />
        <Banner />
        <Footer />
    </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Header from "@/components/Header";
import Banner from "@/components/Banner";
import Footer from "@/components/Footer";

export default {
  name: 'HomeView',
  components: {
    // HelloWorld,
      Header,
      Banner,
      Footer
  },

}
</script>



<!--<template>-->
<!--    <div class="home">-->
<!--        <Header />-->
<!--        <Banner />-->
<!--        <Footer />-->
<!--    </div>-->
<!--</template>-->

<!--<script>-->
<!--    import Header from '@/components/Header'-->
<!--    import Banner from '@/components/Banner'-->
<!--    import Footer from '@/components/Footer'-->

<!--    export default {-->
<!--        name: 'HomeView',-->
<!--        components: {-->
<!--            Header,-->
<!--            Banner,-->
<!--            Footer-->
<!--        },-->
<!--    }-->
<!--</script>-->