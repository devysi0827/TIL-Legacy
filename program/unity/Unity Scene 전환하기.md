# Unity Scene 전환하기

UnityEngine.SceneManagement를 이용하면 쉽게 전환할수 있다.



```c#
using UnityEngine.SceneManagement;

public class MainScript2 : MonoBehaviour
{
   
    public int SolvedQuizLevel = 0;
    public int TotalProblem = 9;
    
    private void Start()
    {
    }

    private void Update()
    {
        if (SolvedQuizLevel >= TotalProblem)
        {
            this._stageClearBox.SetActive(true);
            Invoke("stage3", 3f);
        }
    }

    // 씬 전환 함수
    public void stage3()
    {
        SceneManager.LoadScene("Stage3");
    }
}

```

- SceneManager.LoadScene("Stage3")을 하면 ""내부에 스테이지로 씬 전환을 시킬 수 있다. 이 경우 stage3으로 이동한다.
- 이걸 응용해서 나는 invoke함수와 if문을 섞어서 특정 조건을 만족하면 스테이지가 전환되도록 함수를 작성했다.

