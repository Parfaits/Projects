using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Respawn : MonoBehaviour {

	public Transform spawn;

	public void playerRespawn()
	{
		transform.position = spawn.position;
	}
}
