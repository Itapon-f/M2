/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_size.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 17:09:35 by agiron-d          #+#    #+#             */
/*   Updated: 2025/11/27 17:10:01 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_stack_size(t_stack *stack)
{
	int		count;
	t_stack	*current;

	if (!stack)
		return (0);
	count = 1;
	current = stack->next;
	while (current != stack)
	{
		count++;
		current = current->next;
	}
	return (count);
}
