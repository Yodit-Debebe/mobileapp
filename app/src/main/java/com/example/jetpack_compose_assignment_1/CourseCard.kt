package com.example.jetpack_compose_assignment_1

import androidx.compose.animation.animateContentSize
import androidx.compose.animation.core.tween
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun CourseCard(course: Course) {
    var isExpanded by remember { mutableStateOf(false) }

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
            .animateContentSize(animationSpec = tween(durationMillis = 300)),
             elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)

    ) {
        Column(modifier = Modifier.padding(16.dp)
                                  .clickable { isExpanded = !isExpanded }
        ) {

            Text(text = course.title, style = MaterialTheme.typography.titleMedium)
            Text(text = "Code: ${course.code}")
            Text(text = "Credits: ${course.credits}")

            Spacer(modifier = Modifier.height(8.dp))


            if (isExpanded) {
                Text(text = "Description: ${course.description}")
                Text(text = "Prerequisites: ${course.prerequisites}")

                Spacer(modifier = Modifier.height(8.dp))


                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.End
                ) {
                    Button(onClick = { isExpanded = !isExpanded },
                        colors = ButtonDefaults.buttonColors(
                            containerColor = MaterialTheme.colorScheme.secondary
                        ))  {
                        Text(text = "Less", color = MaterialTheme.colorScheme.onSecondary)
                    }
                }
            } else {

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.End
                ) {
                    Button(onClick = { isExpanded = !isExpanded },
                        colors = ButtonDefaults.buttonColors(
                            containerColor = MaterialTheme.colorScheme.secondary // Using theme color
                        )) {
                        Text(text = "More", color = MaterialTheme.colorScheme.onSecondary)
                    }
                }
            }
        }
    }
}