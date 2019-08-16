using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour 
{

	public GameObject player;

	public Transform left;
	public Transform right;
	// Use this for initialization
	void Start () 
	{
		
	}
	
	// Update is called once per frame
	void Update () 
	{
		Vector3 newPosition = transform.position;
		newPosition.x = player.transform.position.x;
		newPosition.x = Mathf.Clamp (newPosition.x, left.position.x, right.position.x);
		transform.position = newPosition;
	}
}
 