# react-refresh-webpack-plugin

https://github.com/pmmmwh/react-refresh-webpack-plugin



서버를 끄지 않고 저장만으로 webpack의 수정사항을 반영하는 plugin



1. webpack 설치

```javascript
npm i -D @pmmmwh/react-refresh-webpack-plugin react-refresh
```

2. webpack 서버 설치

```javascript
npm i -D webpack-dev-server 
```

3. package.json 설정

```javascript
 "scripts": {
    "dev": "webpack serve --env development"
  },
```

4. webpack.config.js

```javascript
//최상단
const RefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin')

...

options: {
                presets:['@babel/preset-env', '@babel/preset-react'],
                plugins: ['@babel/plugin-proposal-class-properties','react-refresh/babel'],
            }
...

plugins: [
        new RefreshWebpackPlugin()
    ],
    
...

devServer: {
  puvlicPath: '/dist/',
  hot : true,
}
```

