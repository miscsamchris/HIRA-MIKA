using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TouchManager : MonoBehaviour {
    private bool flag = false;
	void Update () {
        if (Input.GetMouseButtonDown(0) && Input.touches[0].phase==TouchPhase.Began && flag==false)
        {
            flag = true;
            VoidAR.GetInstance().startMarkerlessTracking();

        }
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            flag = false;
            VoidAR.GetInstance().resetMarkerless();
        }
    }
}
