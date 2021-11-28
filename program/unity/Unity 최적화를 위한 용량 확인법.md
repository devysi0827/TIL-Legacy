# Unity 최적화를 위한 용량 확인법

1. build를 완료한다.
2. navbar Window > general > Console > 오른쪽 상단 ... 세개 > Open Editor Log
3. 중후반에 build report를 살펴서 불필요한 파일을 정리하자!

```
Build Report
Uncompressed usage by category (Percentages based on user generated assets only):
Textures               362.2 mb	 82.3% 
Meshes                 15.3 mb	 3.5% 
Animations             825.6 kb	 0.2% 
Sounds                 0.0 kb	 0.0% 
Shaders                19.4 mb	 4.4% 
Other Assets           4.9 mb	 1.1% 
Levels                 23.1 mb	 5.2% 
Scripts                1.2 mb	 0.3% 
Included DLLs          13.3 mb	 3.0% 
File headers           39.9 kb	 0.0% 
Total User Assets      440.2 mb	 100.0% 
Complete build size    549.3 mb
Used Assets and files from the Resources folder, sorted by uncompressed size:
 16.9 mb	 3.1% Assets/Fonts/NEXON Lv2 Gothic Medium SDF.asset  v
 16.9 mb	 3.1% Resources/unity_builtin_extra
 ....
생략
....
```

