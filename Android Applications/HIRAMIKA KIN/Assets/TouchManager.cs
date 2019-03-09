using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TouchManager : MonoBehaviour {
    private bool flag = false;
    private ApiAiModule a;
    void Start()
    {
        a = transform.GetComponent<ApiAiModule>();
        flag = false;
    }
    void Update () {
        if (Input.GetMouseButton(0) && Input.touches[0].phase == TouchPhase.Began && flag == false)
        {
            VoidAR.GetInstance().startMarkerlessTracking();
            flag = true;

        }
        if (Input.GetMouseButton(0) && Input.touches[0].phase == TouchPhase.Began && flag)
        {
            a.StartNativeRecognition();
        }
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            VoidAR.GetInstance().resetMarkerless();
            flag = false;

        }
    }
}
