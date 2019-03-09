using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
// Standard Loading screen
public class LoadingScreen : MonoBehaviour
{
    public Transform LoadingBar;
    public Image screen;
    [SerializeField] private float currentAmount = 0;
    [SerializeField] private float speed = 14.0f;
    void Update()
    {
        if (currentAmount < 100)
        {
            currentAmount += speed * Time.deltaTime;
            Debug.Log((int)currentAmount);
        }
        else
        {
            screen.CrossFadeColor(Color.black, 1.0f, true, true);
            SceneManager.LoadScene("AR");   
        }

        LoadingBar.GetComponent<Image>().fillAmount = currentAmount / 100;
    }
}