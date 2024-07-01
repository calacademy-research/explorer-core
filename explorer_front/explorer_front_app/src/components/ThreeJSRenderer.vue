<template>
  <div ref="sceneContainer" class="scene-container"></div>
</template>

<script>
import * as THREE from 'three';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import { MTLLoader } from 'three/examples/jsm/loaders/MTLLoader';

export default {
  name: 'ObjViewer',
  mounted() {
    this.initThreeJS();
  },
  methods: {
    initThreeJS() {
      // Set up the scene
      const scene = new THREE.Scene();

      // Set up the camera
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.z = 5;

      // Set up the renderer
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      this.$refs.sceneContainer.appendChild(renderer.domElement);

      // Set up lighting
      const ambientLight = new THREE.AmbientLight(0x404040); // soft white light
      scene.add(ambientLight);

      const pointLight = new THREE.PointLight(0xffffff, 1, 100);
      pointLight.position.set(10, 10, 10);
      scene.add(pointLight);

      const objPath = encodeURI('assets/CAS 8141.obj');
      const mtlPath = encodeURI('assets/CAS 8141.mtl');
      console.log(objPath);
      console.log(mtlPath);

      // Load the .mtl file and then the .obj file
      const mtlLoader = new MTLLoader();
      mtlLoader.load(mtlPath, (materials) => {
        materials.preload();

        const objLoader = new OBJLoader();
        objLoader.setMaterials(materials);
        objLoader.load(
          objPath,
          (object) => {
            object.position.set(0, 0, 0); // Adjust position
            object.scale.set(1, 1, 1); // Adjust scale
            scene.add(object);
            console.log('Object loaded and added to the scene');
          },
          (xhr) => {
            console.log((xhr.loaded / xhr.total) * 100 + '% loaded');
          },
          (error) => {
            console.error('An error happened', error);
          }
        );
      });

      // Add a simple cube for debugging
      const geometry = new THREE.BoxGeometry();
      const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
      const cube = new THREE.Mesh(geometry, material);
      cube.position.set(0, 0, -2);
      scene.add(cube);

      // Animation loop
      const animate = () => {
        requestAnimationFrame(animate);

        // Rotate the object (optional)
        // if (object) {
        //   object.rotation.x += 0.01;
        //   object.rotation.y += 0.01;
        // }

        renderer.render(scene, camera);
      };
      animate();

      // Handle window resize
      window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
      });
    },
  },
};
</script>

<style>
.scene-container {
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
</style>
