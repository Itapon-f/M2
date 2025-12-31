/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_remove_first.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 17:08:57 by agiron-d          #+#    #+#             */
/*   Updated: 2025/11/27 17:09:21 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*ft_stack_remove_first(t_stack **stack)
{
	t_stack	*first;

	if (!stack || !*stack)
		return (NULL);
	first = *stack;
	if (first->next == first)
	{
		*stack = NULL;
		first->next = NULL;
		first->prev = NULL;
		return (first);
	}
	*stack = first->next;
	first->prev->next = *stack;
	(*stack)->prev = first->prev;
	first->next = NULL;
	first->prev = NULL;
	return (first);
}
