using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour 
{
	//used as reference
	private Rigidbody2D rb2d;

	public Vector2 jumpHeight;
	public float speed;

	bool Grounded = false;

	public Transform botGroundCheck;
	//public Transform leftWallCheck;
	//public Transform rightWallCheck;

	float groundRadius = 1.0f;
	public LayerMask whatIsGround;
	//public LayerMask whatIsWall;
	// Use this for initialization
	void Start () 
	{
		rb2d = GetComponent<Rigidbody2D> ();
	}
	
	// Update is called once per frame
	void FixedUpdate ()
	{
		Grounded = Physics2D.OverlapCircle (botGroundCheck.position, groundRadius, whatIsGround);
		//leftWalled = Physics2D.OverlapCircle (leftWallCheck.position, groundRadius, whatIsWall);
		//rightWalled = Physics2D.OverlapCircle (rightWallCheck.position, groundRadius, whatIsWall);

		//moves the player according to the inputs given by the player
		float moveHorizontal = Input.GetAxis ("Horizontal");

		rb2d.velocity = new Vector2 (moveHorizontal * speed,rb2d.velocity.y);
	}

	void Update()
	{
		if (Input.GetButtonDown ("Jump") && (Grounded)) 
		{
			if (Grounded) {
				if(rb2d.gravityScale > 0)
			{
				rb2d.AddForce(-jumpHeight, ForceMode2D.Impulse);
			} 
			else
			{
				rb2d.AddForce(jumpHeight,ForceMode2D.Impulse);
			}
		}
	}
		if(Input.GetButtonDown ("switchGravity"))
		{
				rb2d.gravityScale = rb2d.gravityScale * -1;
		}
	}
}