<script lang="ts">
import { defineComponent } from 'vue';
import { SideBar, SideButton, SideSection, WindowFrame } from '@vasakgroup/vue-libvasak';
import routers from '@/routers/index';



export default defineComponent({
  name: 'App',
  data() {
    return {
      routers,
      section: 'INFO'
    };
  },
  methods: {
    changeSection(section: string) {
      console.log('changeSection', section);
      return this.section = section;
    }
  },
  computed: {
    routerComponent() {
      return this.routers.find((r:any) => r.tag === this.section)?.component;
    }

  },
  components: {
    SideBar,
    SideButton,
    SideSection,
    WindowFrame
  }
});
</script>

<template>
  <WindowFrame title="Vasak">
    <div class="container-fluid">
      <div class="row flex-nowarp">
        <SideBar>
          <SideSection>
            <template v-for="router in routers" :key="router.tag">
              <SideButton
                :title="router.title"
                :image="router.image"
                @click="changeSection(router.tag)"
              />
            </template>
          </SideSection>
          <SideSection>
            <SideButton
              title="Link"
              image="https://via.placeholder.com/32"
              exec="https://google.com"
            />
          </SideSection>
        </SideBar>

        <div class="p-3 col side-content-area">
          <component :is="routerComponent" />
        </div>
      </div>
    </div>
  </WindowFrame>
</template>

<style>
.side-content-area{
  height: calc(100vh - 30px);
  overflow: auto;
}
</style>