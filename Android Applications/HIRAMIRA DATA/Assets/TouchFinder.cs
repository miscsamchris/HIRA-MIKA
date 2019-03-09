using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class TouchFinder : MonoBehaviour {
    public Text t;
	void Start () {
        t.text= PlayerPrefs.GetString("BED", "001"); 
    }

    void Update()
    {
        if (Input.GetMouseButton(0))
        {
            SceneManager.LoadScene("DataEntry");
        }
    }
}
