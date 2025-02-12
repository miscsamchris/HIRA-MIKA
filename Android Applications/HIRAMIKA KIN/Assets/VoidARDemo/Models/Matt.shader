﻿Shader "FX/Matte Shadow" 
{   
	Properties {     
	_Color ("Main Color", Color) = (1,1,1,1)     
	_MainTex ("Base (RGB) Trans (A)", 2D) = "white" {}     
	_Cutoff ("Alpha cutoff", Range(0,1)) = 0.5 
	}   
	SubShader {       
		Tags {"Queue"="Geometry-100" "IgnoreProjector"="True" "RenderType"="TransparentCutout"}     
		LOD 200    
		Blend Zero SrcColor   
		CGPROGRAM   
		#pragma surface surf ShadowOnly alphatest:_Cutoff   
		fixed4 _Color;   
		struct Input {     
			float2 uv_MainTex; 
		};   
		inline fixed4 LightingShadowOnly (SurfaceOutput s, fixed3 lightDir, fixed atten) {
		//discard;
		     fixed4 c;     
		     c.rgb = s.Albedo*atten;    
		     c.a = s.Alpha;
		     if(c.b != 231/255 || c.g != 95/255){
		     	//discard;       
		     }
		     return c; 
		}   
		void surf (Input IN, inout SurfaceOutput o)  {
			//discard;       
			fixed4 c = _Color;      
			o.Albedo = c.rgb;     
			o.Alpha = 1;   
		}   
		ENDCG   
	}   
	Fallback "Transparent/Cutout/VertexLit"   
}