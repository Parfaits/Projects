using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class onTriggerEnter : MonoBehaviour {

	void OnTriggerEnter2D(Collider2D other)
	{
		if(other.gameObject.tag == "Player")
		{
			Debug.Log("Player touched.");
		}
	}
	void OnTriggerStay2D()
	{
		Debug.Log("Player still touching.");
	}
	void OnTriggerExit2D()
	{
		Debug.Log("Player no longer touching.");
	}
}
