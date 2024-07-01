# explorer_front_app

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# 3D Scan Objects Rendering - ThreeJSRenderer.vue
## Scans setup
Place .obj, .mtl, and .jpg files (file names for CAS 8141 currently hardcoded in code for testing) into explorer_front_app/public/assets

## Debugging, notes
Currently, the scan is not rendering in the ThreeJS scene. The files are fully loading (check console logs, should count up to 100%) but not rendering in the scene, a simple green cube is rendering correctly. There could be an issue rendering due to size of files, looking into it still. -jz
